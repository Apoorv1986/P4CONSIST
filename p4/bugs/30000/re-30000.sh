#!/bin/bash

#------------------------------------------------ VLAN 10 --------------------------------------------------
echo "================================ -- S1 10 -- =====================================\n"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_modify MyIngress.ipv4_lpm MyIngress.ipv4_forward 29996 00:00:00:00:02:01 1 29996
EOD
#------------------------------------------------ VLAN 20 --------------------------------------------------
echo "================================ -- S1 20 -- =====================================\n"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_modify MyIngress.ipv4_lpm MyIngress.ipv4_forward 29997 00:00:00:00:02:01 1 29997
EOD
#------------------------------------------------ VLAN 30 --------------------------------------------------
echo "================================ -- S1 30 -- =====================================\n"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_modify MyIngress.ipv4_lpm MyIngress.ipv4_forward 29998 00:00:00:00:02:01 1 29998
EOD
#------------------------------------------------ VLAN 40 --------------------------------------------------
echo "================================ -- S1 40 -- =====================================\n"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_modify MyIngress.ipv4_lpm MyIngress.ipv4_forward 29999 00:00:00:00:02:01 1 29999
EOD

#------------------------------------------------ VLAN 50 --------------------------------------------------
echo "================================ -- S1 50 -- =====================================\n"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_modify MyIngress.ipv4_lpm MyIngress.ipv4_forward 29995 00:00:00:00:02:01 1 29995
EOD
