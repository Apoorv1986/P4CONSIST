#!/bin/bash

echo "S2"
simple_switch_CLI --thrift-port 9092 --thrift-ip 10.10.1.102 --pre SimplePreLAG <<EOD
table_num_entries MyIngress.ipv4_lpm
EOD

echo "S3"
simple_switch_CLI --thrift-port 9093 --thrift-ip 10.10.1.103 --pre SimplePreLAG <<EOD
table_num_entries MyIngress.ipv4_lpm
EOD

echo "S4"
simple_switch_CLI --thrift-port 9094 --thrift-ip 10.10.1.104 --pre SimplePreLAG <<EOD
table_num_entries MyIngress.ipv4_lpm
EOD

echo "S1"
simple_switch_CLI --thrift-port 9090 --thrift-ip 10.10.1.101 --pre SimplePreLAG <<EOD
table_num_entries MyIngress.ipv4_lpm
EOD
