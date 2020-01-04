#!/bin/sh

sudo modprobe 8021q
#sudo vconfig add enp0s8 5
sudo service networking restart
