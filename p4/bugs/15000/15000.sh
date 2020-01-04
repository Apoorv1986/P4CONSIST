#!/bin/bash

#------------------------------------------------ VLAN 10 --------------------------------------------------
echo "================================ -- S1 10 -- =====================================\n"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_modify MyIngress.ipv4_lpm MyIngress.ipv4_forward 14996 00:00:00:00:03:01 2 14996
EOD
#------------------------------------------------ VLAN 20 --------------------------------------------------
echo "================================ -- S1 20 -- =====================================\n"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_modify MyIngress.ipv4_lpm MyIngress.ipv4_forward 14997 00:00:00:00:03:01 2 14997
EOD
#------------------------------------------------ VLAN 30 --------------------------------------------------
echo "================================ -- S1 30 -- =====================================\n"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_modify MyIngress.ipv4_lpm MyIngress.ipv4_forward 14998 00:00:00:00:03:01 2 14998
EOD
#------------------------------------------------ VLAN 40 --------------------------------------------------
echo "================================ -- S1 40 -- =====================================\n"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_modify MyIngress.ipv4_lpm MyIngress.ipv4_forward 14999 00:00:00:00:03:01 2 14999
EOD
#------------------------------------------------ VLAN 50 --------------------------------------------------
echo "================================ -- S1 50 -- =====================================\n"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_modify MyIngress.ipv4_lpm MyIngress.ipv4_forward 14995 00:00:00:00:03:01 2 14995
EOD
#echo "\n================================ -- S3 -- ===================================\n"
#simple_switch_CLI --thrift-port 9093 --thrift-ip 10.10.1.103 --pre SimplePreLAG <<EOD
#table_add MyIngress.ipv4_lpm MyIngress.ipv4_forward 172.16.40.0/24 50 1 => 00:00:00:00:04:03 2 15004
#EOD



time=$(date +"%M:%S.%6N")
echo "$time" > /vagrant/experiment/bug_insertion_15000.log
