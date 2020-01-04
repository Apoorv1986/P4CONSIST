#!/usr/bin/python

import csv
import subprocess
import sys
from datetime import datetime

detectionTime = []
FMT = '%M:%S.%f'

output_sink1 = "output_sink1"
output_sink2 = "output_sink2"
output_sink3 = "output_sink3"
output_sink4 = "output_sink4"

# Parsing start times
output1 = open(output_sink1, "rw+")
output2 = open(output_sink2, "rw+")
output3 = open(output_sink3, "rw+")
output4 = open(output_sink4, "rw+")

list_outputs = [output1, output2, output3, output4]

for output in list_outputs:

    vlan10 = False
    vlan20 = False
    vlan30 = False
    vlan40 = False
    vlan50 = False

    for line in output:
        tmp = 0
        line = line.replace("\n", "") # removing line breaks
        if "vlan 10 ------> Inconsistent" in line and not vlan10:
            tmp = line.split('=')
            detectionTime.append(tmp[1]) # production start time
            vlan10 = True

        if "vlan 20 ------> Inconsistent" in line and not vlan20:
            tmp = line.split('=')
            detectionTime.append(tmp[1]) # production start time
            vlan20 = True

        if "vlan 30 ------> Inconsistent" in line and not vlan30:
            tmp = line.split('=')
            detectionTime.append(tmp[1]) # production start time
            vlan30 = True

        if "vlan 40 ------> Inconsistent" in line and not vlan40:
            tmp = line.split('=')
            detectionTime.append(tmp[1]) # production start time
            vlan40 = True

        if "vlan 50 ------> Inconsistent" in line and not vlan50:
            tmp = line.split('=')
            detectionTime.append(tmp[1]) # production start time
            vlan50 = True

        if vlan10 and vlan20 and vlan30 and vlan40 and vlan50:
            break

output1.close()
output2.close()
output3.close()
output4.close()

#print ("%s, %s, %s" % (prod, diff, exhaus))
detectionTime.sort()
#print("detectionTime: %s" % detectionTime)
# Parsing Detection and Localization times
detection_delta_list = []

with open(sys.argv[1]) as bugFile:
    for line in bugFile:
        line = line.replace("\n", "")
        print("bug: %s" % line)
        for time in detectionTime:
            detection_delta = 0
            detection_delta = datetime.strptime(time, FMT) - datetime.strptime(line, FMT)
            detection_delta = detection_delta.total_seconds()
            #print("%s" % ('{0:.6f}'.format(detection_delta)))
            detection_delta_list.append('{0:.6f}'.format(detection_delta))


print("detectionTime: %s" % detection_delta_list)
