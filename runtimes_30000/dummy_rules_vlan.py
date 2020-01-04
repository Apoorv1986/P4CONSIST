#!/usr/bin/env python

import sys
import json

with open(sys.argv[1], 'a') as jsonfile:
    rule = 0
    for i in range(1, 121):
        for j in range(1, 251):
            jsonfile.write('{\n')
            jsonfile.write('"table": "MyIngress.ipv4_lpm",\n')
            jsonfile.write('"match": {\n')
            jsonfile.write('"hdr.ipv4.dstAddr": ["10.10.%d.%d", 32],\n' % (i, j))
            jsonfile.write('"hdr.dot12q.vlan": 1,\n')
            jsonfile.write('"standard_metadata.ingress_port": 3\n')
            jsonfile.write('},\n')
            jsonfile.write('"action_name": "MyIngress.ipv4_forward",\n')
            jsonfile.write('"action_params": {\n')
            jsonfile.write('"dstAddr": "00:00:00:00:00:00",\n')
            jsonfile.write('"port": 1,\n')
            jsonfile.write('"rule": %d\n' % rule)
            jsonfile.write('}\n')
            if i == 120 and j == 250:
                jsonfile.write('}\n')
            else:
                jsonfile.write('},\n')
            rule = rule + 1
    jsonfile.write(']\n}')
