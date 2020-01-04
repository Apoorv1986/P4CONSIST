#!/bin/bash

#vagrant ssh src1 -c 'sudo kill -9  $(ps aux | grep '\''[t]cpreplay'\'' | awk '\''{print $2}'\'')'
vagrant ssh src1 -c 'sudo kill -9 $(ps aux | grep '\''[s]udo tcpreplay'\'' | awk '\''{print $2}'\'')'&

#vagrant ssh src2 -c 'sudo kill -9  $(ps aux | grep '\''[t]cpreplay'\'' | awk '\''{print $2}'\'')'
vagrant ssh src2 -c 'sudo kill -9 $(ps aux | grep '\''[s]udo tcpreplay'\'' | awk '\''{print $2}'\'')'&

#vagrant ssh src3 -c 'sudo kill -9  $(ps aux | grep '\''[t]cpreplay'\'' | awk '\''{print $2}'\'')'
vagrant ssh src3 -c 'sudo kill -9 $(ps aux | grep '\''[s]udo tcpreplay'\'' | awk '\''{print $2}'\'')'&

#vagrant ssh src4 -c 'sudo kill -9  $(ps aux | grep '\''[t]cpreplay'\'' | awk '\''{print $2}'\'')'
vagrant ssh src4 -c 'sudo kill -9 $(ps aux | grep '\''[s]udo tcpreplay'\'' | awk '\''{print $2}'\'')'&

#vagrant ssh src5 -c 'sudo kill -9  $(ps aux | grep '\''[t]cpreplay'\'' | awk '\''{print $2}'\'')'
vagrant ssh src5 -c 'sudo kill -9 $(ps aux | grep '\''[s]udo tcpreplay'\'' | awk '\''{print $2}'\'')'&
