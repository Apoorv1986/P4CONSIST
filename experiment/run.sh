#!/bin/bash

vagrant ssh src1 -c 'sudo  tcpreplay --loop=1 --enable-file-cache --preload-pcap --pps=1000 --pps-multi=1000 --intf1=enp0s8 /vagrant/experiment/pcaps/10.pcap'&
vagrant ssh src2 -c 'sudo  tcpreplay --loop=1 --enable-file-cache --preload-pcap --pps=1000 --pps-multi=1000 --intf1=enp0s8 /vagrant/experiment/pcaps/20.pcap'&
vagrant ssh src3 -c 'sudo  tcpreplay --loop=1 --enable-file-cache --preload-pcap --pps=1000 --pps-multi=1000 --intf1=enp0s8 /vagrant/experiment/pcaps/30.pcap'&
vagrant ssh src4 -c 'sudo  tcpreplay --loop=1 --enable-file-cache --preload-pcap --pps=1000 --pps-multi=1000 --intf1=enp0s8 /vagrant/experiment/pcaps/40.pcap'&
vagrant ssh src5 -c 'sudo  tcpreplay --loop=1 --enable-file-cache --preload-pcap --pps=1000 --pps-multi=1000 --intf1=enp0s8 /vagrant/experiment/pcaps/50.pcap'&
