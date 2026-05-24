# OpenDev GW2ALV18 FPGA PINs

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
| Keys    |                                                        |                                  |
| P10     | IO_TYPE=LVCMOS33 PULL_MODE=NONE BANK_VCCIO=3.3         | key[0], key_0, key0              |
| R10     | IO_TYPE=LVCMOS33 PULL_MODE=NONE BANK_VCCIO=3.3         | key[1], key_1, key1              |
| M9      | IO_TYPE=LVCMOS33 PULL_MODE=NONE BANK_VCCIO=3.3         | key[2], key_2, key2              |
| N11     | IO_TYPE=LVCMOS33 PULL_MODE=NONE BANK_VCCIO=3.3         | key[3], key_3, key3              |
| IIC     |                                                        |                                  |
| P6      | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | iic_scl                          |
| N6      | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | iic_sda                          |
| SDCard  |                                                        |                                  |
| M11     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | sd_clk                           |
| R7      | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | sd_cs_n                          |
| B10     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | sd_mosi                          |
| A13     | IO_TYPE=LVCMOS33 PULL_MODE=UP BANK_VCCIO=3.3           | sd_miso                          |
| Uart    |                                                        |                                  |
| N10     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | uart_tx, tx                      |
| P7      | IO_TYPE=LVCMOS33 PULL_MODE=UP BANK_VCCIO=3.3           | uart_rx, rx                      |
| LED     |                                                        |                                  |
| C9      | IO_TYPE=LVCMOS33 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=3.3 | led[0], led_0, led0              |
| A9      | IO_TYPE=LVCMOS33 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=3.3 | led[1], led_1, led1              |
| D11     | IO_TYPE=LVCMOS33 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=3.3 | led[2], led_2, led2              |
| K14     | IO_TYPE=LVCMOS33 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=3.3 | led[3], led_3, led3              |
| DDR     |                                                        |                                  |
| H4      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_ba[0], ddr_ba[0]           |
| D3      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_ba[1], ddr_ba[1]           |
| H5      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_ba[2], ddr_ba[2]           |
| E8      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_addr[0], ddr_addr[0]       |
| A4      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_addr[1], ddr_addr[1]       |
| D6      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_addr[2], ddr_addr[2]       |
| D9      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_addr[3], ddr_addr[3]       |
| B5      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_addr[4], ddr_addr[4]       |
| D7      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_addr[5], ddr_addr[5]       |
| B1      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_addr[6], ddr_addr[6]       |
| E9      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_addr[7], ddr_addr[7]       |
| A5      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_addr[8], ddr_addr[8]       |
| E11     | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_addr[9], ddr_addr[9]       |
| K3      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_addr[10], ddr_addr[10]     |
| C7      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_addr[11], ddr_addr[11]     |
| A3      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_addr[12], ddr_addr[12]     |
| A8      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_addr[13], ddr_addr[13]     |
| R3      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_odt, ddr_odt               |
| J2      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_cke, ddr_cke               |
| L2      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_we_n, ddr_we_n             |
| R6      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_cas_n, ddr_cas_n           |
| R4      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_ras_n, ddr_ras_n           |
| P5      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_cs_n, ddr_cs_n             |
| A10     | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_rst_n, ddr_rst_n           |
| G1      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_dqm[0], ddr_dqm[0]         |
| K5      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | o_ddr_dqm[1], ddr_dqm[1]         |
| G5      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[0], ddr_dq[0]          |
| F5      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[1], ddr_dq[1]          |
| F4      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[2], ddr_dq[2]          |
| F3      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[3], ddr_dq[3]          |
| E2      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[4], ddr_dq[4]          |
| C1      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[5], ddr_dq[5]          |
| E1      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[6], ddr_dq[6]          |
| B3      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[7], ddr_dq[7]          |
| M3      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[8], ddr_dq[8]          |
| K4      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[9], ddr_dq[9]          |
| N2      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[10], ddr_dq[10]        |
| L1      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[11], ddr_dq[11]        |
| P4      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[12], ddr_dq[12]        |
| H3      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[13], ddr_dq[13]        |
| R1      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[14], ddr_dq[14]        |
| M2      | IO_TYPE=SSTL15 PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5   | io_ddr_dq[15], ddr_dq[15]        |
| J1,J3   | IO_TYPE=SSTL15D PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5  | o_ddr_clk, ddr_clk               |
| G2,G3   | IO_TYPE=SSTL15D PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5  | o_ddr_dqs[0], ddr_dqs[0]         |
| J5,K6   | IO_TYPE=SSTL15D PULL_MODE=NONE DRIVE=8 BANK_VCCIO=1.5  | o_ddr_dqs[1], ddr_dqs[1]         |
| LCD     |                                                        |                                  |
| D10     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[0]                       |
| E10     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[1]                       |
| F10     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[2]                       |
| N14     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[3]                       |
| N16     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[4]                       |
| L12     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[5]                       |
| J11     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[6]                       |
| L14     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[7]                       |
| C11     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[8]                       |
| A11     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[9]                       |
| A15     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[10]                      |
| B14     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[11]                      |
| B13     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[12]                      |
| A14     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[13]                      |
| C12     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[14]                      |
| B12     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[15]                      |
| E15     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[16]                      |
| K15     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[17]                      |
| P16     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[18]                      |
| N15     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[19]                      |
| K11     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[20]                      |
| D14     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[21]                      |
| B11     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[22]                      |
| A12     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rgb[23]                      |
| M15     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_hs                           |
| M14     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_vs                           |
| K12     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_de                           |
| K13     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_bl                           |
| L16     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_clk                          |
| P15     | IO_TYPE=LVCMOS33 PULL_MODE=UP DRIVE=8 BANK_VCCIO=3.3   | lcd_rst_n                        |
