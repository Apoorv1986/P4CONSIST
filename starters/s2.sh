#!/bin/bash
echo "Starting s2 ..."
vagrant ssh s2 -c 'sudo simple_switch_grpc --device-id 2 -i 1@enp0s9 -i 2@enp0s10 -i 3@enp0s16 --thrift-port 9092 --no-p4 -- --grpc-server-addr 0.0.0.0:50051'
sleep 5
