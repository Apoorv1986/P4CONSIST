#!/bin/bash
echo "Starting s3 ..."
vagrant ssh s3 -c 'sudo simple_switch_grpc --device-id 3 -i 1@enp0s9 -i 2@enp0s10 -i 3@enp0s16 --thrift-port 9093 --no-p4 -- --grpc-server-addr 0.0.0.0:50051'
sleep 5
