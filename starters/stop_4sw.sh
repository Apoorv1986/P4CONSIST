#!/bin/bash
echo "Stopping the switches ..."

vagrant ssh s1 -c 'sudo kill -9  $(ps aux | grep '\''[s]imple_switch_grpc'\'' | awk '\''{print $2}'\'')'
vagrant ssh s1 -c 'sudo kill -9  $(ps aux | grep '\''[s]udo simple_switch_grpc'\'' | awk '\''{print $2}'\'')'

vagrant ssh s2 -c 'sudo kill -9  $(ps aux | grep '\''[s]imple_switch_grpc'\'' | awk '\''{print $2}'\'')'
vagrant ssh s2 -c 'sudo kill -9  $(ps aux | grep '\''[s]udo simple_switch_grpc'\'' | awk '\''{print $2}'\'')'

vagrant ssh s3 -c 'sudo kill -9  $(ps aux | grep '\''[s]imple_switch_grpc'\'' | awk '\''{print $2}'\'')'
vagrant ssh s3 -c 'sudo kill -9  $(ps aux | grep '\''[s]udo simple_switch_grpc'\'' | awk '\''{print $2}'\'')'

vagrant ssh s4 -c 'sudo kill -9  $(ps aux | grep '\''[s]imple_switch_grpc'\'' | awk '\''{print $2}'\'')'
vagrant ssh s4 -c 'sudo kill -9  $(ps aux | grep '\''[s]udo simple_switch_grpc'\'' | awk '\''{print $2}'\'')'
