#!/bin/bash
echo "Starting s1 ..."
vagrant ssh s1 -c 'sudo simple_switch_grpc --device-id 1 -i 1@enp0s9 -i 2@enp0s10 -i 3@enp0s16 --thrift-port 9090 --no-p4 -- --grpc-server-addr 0.0.0.0:50051'
sleep 5
