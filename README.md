# GOWIN FPGA Floor Planner Tool

[中文](README.zh.md)

Generate GoWin FPGA floor planner file:

```
$ python3 floor_planner.py \
  -md OpenDev_GW2ALV18.md \
  -v test/top.v           \
  -cst test/hdmi.cst
```

## IO Ports Description File

The IO ports are defined in Markdown file as table:

| Port    | IO Type                                                | Names                            |
|---------|--------------------------------------------------------|----------------------------------|
| Sys     |                                                        |                                  |
| T7      | IO_TYPE=LVCMOS33 PULL_MODE=UP BANK_VCCIO=3.3           | sys_clk, clk                     |
| M7      | IO_TYPE=LVCMOS33 PULL_MODE=UP BANK_VCCIO=3.3           | sys_rst_n, rst_n                 |
| HDMI    |                                                        |                                  |
| R13,T14 | IO_TYPE=LVDS25 PULL_MODE=NONE DRIVE=3.5 BANK_VCCIO=2.5 | o_tmds_clk_p, tmds_clk_p         |
| R11,T12 | IO_TYPE=LVDS25 PULL_MODE=NONE DRIVE=3.5 BANK_VCCIO=2.5 | o_tmds_data_p[0], tmds_data_p[0] |
| P12,T13 | IO_TYPE=LVDS25 PULL_MODE=NONE DRIVE=3.5 BANK_VCCIO=2.5 | o_tmds_data_p[1], tmds_data_p[1] |
| R12,P13 | IO_TYPE=LVDS25 PULL_MODE=NONE DRIVE=3.5 BANK_VCCIO=2.5 | o_tmds_data_p[2], tmds_data_p[2] |
| ...     | ...                                                    | ...                              |

The script extracts the ports from top module and generate the `.cst` file by name matching:

```
$ python3 floor_planner.py -md OpenDev_GW2ALV18.md -v test/top.v -cst test/hdmi.cst

IO_LOC "sys_clk" T7;
IO_PORT "sys_clk" IO_TYPE=LVCMOS33 PULL_MODE=UP BANK_VCCIO=3.3;

IO_LOC "sys_rst_n" M7;
IO_PORT "sys_rst_n" IO_TYPE=LVCMOS33 PULL_MODE=UP BANK_VCCIO=3.3;

IO_LOC "tmds_clk_p" R13,T14;
IO_PORT "tmds_clk_p" IO_TYPE=LVDS25 PULL_MODE=NONE DRIVE=3.5 BANK_VCCIO=2.5;

// diff_port: tmds_clk_n <--> tmds_clk_p

IO_LOC "tmds_data_p[0]" R11,T12;
IO_PORT "tmds_data_p[0]" IO_TYPE=LVDS25 PULL_MODE=NONE DRIVE=3.5 BANK_VCCIO=2.5;

IO_LOC "tmds_data_p[1]" P12,T13;
IO_PORT "tmds_data_p[1]" IO_TYPE=LVDS25 PULL_MODE=NONE DRIVE=3.5 BANK_VCCIO=2.5;

IO_LOC "tmds_data_p[2]" R12,P13;
IO_PORT "tmds_data_p[2]" IO_TYPE=LVDS25 PULL_MODE=NONE DRIVE=3.5 BANK_VCCIO=2.5;

// diff_port: tmds_data_n[0] <--> tmds_data_p[0]

// diff_port: tmds_data_n[1] <--> tmds_data_p[1]

// diff_port: tmds_data_n[2] <--> tmds_data_p[2]
```

Diff port is auto-detected by script.
