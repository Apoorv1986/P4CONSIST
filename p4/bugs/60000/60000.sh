#!/bin/bash

#------------------------------------------------ VLAN 10 --------------------------------------------------
echo "================================ -- S1 10 -- =====================================\n"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_modify MyIngress.ipv4_lpm MyIngress.ipv4_forward 59995 00:00:00:00:03:01 2 59995
EOD
#------------------------------------------------ VLAN 20 --------------------------------------------------
echo "================================ -- S1 20 -- =====================================\n"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_modify MyIngress.ipv4_lpm MyIngress.ipv4_forward 59996 00:00:00:00:03:01 2 59996
EOD
#------------------------------------------------ VLAN 30 --------------------------------------------------
echo "================================ -- S1 30 -- =====================================\n"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_modify MyIngress.ipv4_lpm MyIngress.ipv4_forward 59997 00:00:00:00:03:01 2 59997
EOD
#------------------------------------------------ VLAN 40 --------------------------------------------------
echo "================================ -- S1 40 -- =====================================\n"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_modify MyIngress.ipv4_lpm MyIngress.ipv4_forward 59998 00:00:00:00:03:01 2 59998
EOD
#------------------------------------------------ VLAN 50 --------------------------------------------------
echo "================================ -- S1 50 -- =====================================\n"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_modify MyIngress.ipv4_lpm MyIngress.ipv4_forward 59999 00:00:00:00:03:01 2 59999
EOD

time=$(date +"%M:%S.%6N")
echo "$time" > /vagrant/experiment/bug_insertion_60000.log
