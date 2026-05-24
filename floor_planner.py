#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import argparse

def parse_md_table(file_path):
    table_data = []
    table_row_pattern = re.compile(r'^\s*\|.*\|\s*$')
    separator_pattern = re.compile(r'^\s*\|[\s\-\|:]+\|\s*$')
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if table_row_pattern.match(line):
                if separator_pattern.match(line):
                    continue
                clean_line = line.strip().strip('|')
                cells = tuple(cell.strip() for cell in clean_line.split('|'))
                table_data.append(cells)
    return table_data

def to_port_definition(table_data):
    port_definitions = {}
    pattern = re.compile(r'^[A-Z]{1,2}\d{1,2}(,[A-Z]{1,2}\d{1,2})?$')
    for row in table_data:
        if len(row) == 3:
            port_name = row[0].upper()
            port_type = row[1]
            name_list = row[2].lower()
            if not pattern.match(port_name):
                continue
            var_names = tuple(name.strip() for name in name_list.split(','))
            if len(var_names) == 0:
                print(f"Warning: No variable names found for port {port_name}. Skipping.")
                continue
            for var_name in var_names:
                if var_name in port_definitions:
                    print(f"Warning: Duplicate variable name {var_name}.")
                    continue
                port_definitions[var_name] = (port_name, port_type)
    return port_definitions

import re

def extract_and_expand_ports(verilog_code):
    # remove comments:
    clean_code = re.sub(r'/\*.*?\*/', '', verilog_code, flags=re.DOTALL)
    clean_code = re.sub(r'//.*', '', clean_code)
    # match the ports section of the module declaration:
    ports_section_match = re.search(r'module\s+\w+(?:\s*#\(.*?\))?\s*\((.*?)\);', clean_code, re.DOTALL)
    if not ports_section_match:
        print("Warning: No valid module port declaration structure found.")
        return []
        
    ports_text = ports_section_match.group(1)
    port_pattern = re.compile(
        r'(?:input|output|inout)\s+'
        r'(?:(?:\w+)\s+)*' # type: logic, wire
        r'(?:\[\s*(\d+)\s*:\s*(\d+)\s*\]\s*)?'
        r'(\w+)'
    )

    expanded_ports = []
    # process ports:
    for match in port_pattern.finditer(ports_text):
        msb_str, lsb_str, port_name = match.groups()
        if msb_str is not None and lsb_str is not None:
            msb = int(msb_str)
            lsb = int(lsb_str)
            step = -1 if msb >= lsb else 1
            min_val = min(msb, lsb)
            max_val = max(msb, lsb)
            for i in range(min_val, max_val + 1):
                expanded_ports.append(f"{port_name}[{i}]")
        else:
            expanded_ports.append(port_name)
    return expanded_ports

def get_diff_pair_name(port_name, port_names):
    base_names = []
    if port_name.lower().endswith("_n"):
        base_names = [port_name[:-2] + "_p", port_name[:-2]]
    else:
        pos = port_name.lower().find("_n[")
        if pos > 0:
            base_names = [port_name[:pos] + "_p" + port_name[pos + 2:], port_name[:pos] + port_name[pos + 2:]]
    for base_name in base_names:
        if base_name.lower() in port_names:
            return base_name
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read port definition from Markdown file and update CST file accordingly.")
    parser.add_argument("-md", metavar="<md_file>", required=True, help="Markdown file containing the port definitions.")
    parser.add_argument("-v", metavar="<verilog_file>", required=True, help="Verilog file containing the module declaration.")
    parser.add_argument("-cst", metavar="<cst_file>", required=True, help="CST file to be updated with the port definitions.")

    args = parser.parse_args()
    table_data = parse_md_table(args.md)
    port_definitions = to_port_definition(table_data)
    with open(args.v, 'r', encoding='utf-8') as f:
        verilog_code = f.read()
    port_names = extract_and_expand_ports(verilog_code)
    cst_lines = ["// Auto-generated CST file based on the provided Markdown and Verilog file:", ""]
    for port_name in port_names:
        if port_name.lower() in port_definitions:
            port, port_type = port_definitions[port_name.lower()]
            cst_lines.append(f'IO_LOC "{port_name}" {port};')
            cst_lines.append(f'IO_PORT "{port_name}" {port_type};')
            cst_lines.append("")
        else:
            diff_port = get_diff_pair_name(port_name, port_names)
            if diff_port and (diff_port in port_definitions) and (port_definitions[diff_port][0].find(",") >= 0):
                cst_lines.append(f'// diff_port: {port_name} <--> {diff_port}')
                cst_lines.append("")
            else:
                print(f"Warning: Port {port_name} not found in the Markdown definition. Skipping.")
                continue
    content = "\n".join(cst_lines)
    with open(args.cst, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"CST file '{args.cst}' has been generated:")
    print(content)
