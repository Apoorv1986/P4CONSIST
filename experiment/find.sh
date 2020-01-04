#!/bin/bash
output=$1

if grep -m 1 'vlan 10 ------> Inconsistent' $output; then
    echo "Found! 10"
fi

if grep -m 1 'vlan 20 ------> Inconsistent' $output; then
    echo "Found! 20"
fi

if grep -m 1 'vlan 30 ------> Inconsistent' $output; then
    echo "Found! 30"
fi

if grep -m 1 'vlan 40 ------> Inconsistent' $output; then
    echo "Found! 40"
fi

if grep -m 1 'vlan 50 ------> Inconsistent' $output; then
    echo "Found! 50"
fi

