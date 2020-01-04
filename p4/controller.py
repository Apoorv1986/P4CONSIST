#!/usr/bin/env python2

import argparse
import grpc
import os
import sys
from time import sleep

import p4runtime_lib.bmv2
from p4runtime_lib.switch import ShutdownAllSwitchConnections
import p4runtime_lib.helper
import p4runtime_lib.simple_controller


def printGrpcError(e):
    print "gRPC Error:", e.details(),
    status_code = e.code()
    print "(%s)" % status_code.name,
    traceback = sys.exc_info()[2]
    print "[%s:%d]" % (traceback.tb_frame.f_code.co_filename, traceback.tb_lineno)

def main(sw_name, ip_addr, device_id, grpc_port, p4info_file, runtime_json):
    """ This method will use P4Runtime to program the switch using the
        content of the runtime JSON file as input.
    """
    # Instantiate a P4Runtime helper from the p4info file
    p4info_helper = p4runtime_lib.helper.P4InfoHelper(p4info_file)

    try:
        print('Configuring switch %s using P4Runtime with file %s' % (sw_name, runtime_json))
        with open(runtime_json, 'r') as sw_conf_file:
            outfile = '../logs/%s-p4runtime-requests.txt' % sw_name
            p4runtime_lib.simple_controller.program_switch(
                addr='%s:%d' % (ip_addr, grpc_port),
                device_id=device_id,
                sw_conf_file=sw_conf_file,
                workdir=os.getcwd(),
                proto_dump_fpath=outfile)

    except KeyboardInterrupt:
        print " Shutting down."
    except grpc.RpcError as e:
        printGrpcError(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='P4Runtime Controller')

    parser.add_argument('--switch', help='Name of the switch',
                        type=str, action="store", required=True,
                        default='')
    parser.add_argument('--ip', help='IP Address of the switch',
                        type=str, action="store", required=True,
                        default='')
    parser.add_argument('--id', help='Device ID',
                        type=int, action="store", required=True,
                        default='')
    parser.add_argument('--port', help='gRPC port',
                        type=int, action="store", required=False,
                        default='50051')
    parser.add_argument('--p4info', help='p4info proto in text format from p4c',
                        type=str, action="store", required=True,
                        default='')
    parser.add_argument('--runtime-json', help='Runtime JSON file of the switch',
                        type=str, action="store", required=True,
                        default='')
    args = parser.parse_args()


    if not os.path.exists(args.p4info):
        parser.print_help()
        print "\np4info file not found: %s\n" % args.p4info
        parser.exit(1)
    if not os.path.exists(args.runtime_json):
        parser.print_help()
        print "\nRuntime JSON file: %s  not found!\n" % args.runtime_json
        parser.exit(1)

    main(args.switch, args.ip, args.id, args.port, args.p4info, args.runtime_json)

