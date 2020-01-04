#!/bin/bash
echo "Starting s4 ..."
vagrant ssh s4 -c 'sudo simple_switch_grpc --device-id 4 -i 1@enp0s9 -i 2@enp0s10 -i 3@enp0s16 -i 4@enp0s17 -i 5@enp0s18 -i 6@enp0s19 --thrift-port 9094 --no-p4 -- --grpc-server-addr 0.0.0.0:50051'
sleep 5
