#!/bin/bash
python ../controller.py --switch s1 --ip 10.10.1.101 --id 1 --p4info ../build/mri.p4info --runtime-json  ../../runtimes_30000/s1.json
python ../controller.py --switch s2 --ip 10.10.1.102 --id 2 --p4info ../build/mri.p4info --runtime-json  ../../runtimes_30000/s2.json
python ../controller.py --switch s3 --ip 10.10.1.103 --id 3 --p4info ../build/mri.p4info --runtime-json  ../../runtimes_30000/s3.json
python ../controller.py --switch s4 --ip 10.10.1.104 --id 4 --p4info ../build/mri.p4info --runtime-json  ../../runtimes_30000/s4.json
