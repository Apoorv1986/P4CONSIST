#!/usr/bin/env python
import sys
import struct
import Queue
import logging
import redis
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from threading import Thread
from scapy.all import sniff, sendp, hexdump, get_if_list, get_if_hwaddr
from scapy.all import Packet, IPOption
from scapy.all import PacketListField, ShortField, IntField, LongField, BitField, FieldListField, FieldLenField, ByteField
from scapy.all import Dot1Q, IP, UDP, Raw
from scapy.layers.inet import _IPOption_HDR
from check.verification import Verification

NUM = 0
redis_session = redis.Redis(host='localhost')


def get_if():
    ifs=get_if_list()
    iface=None
    for i in get_if_list():
        if "enp0s8" in i:
            iface=i
            break;
    if not iface:
        print "Cannot find enp0s8 interface"
        exit(1)
    return iface


class SwitchTrace(Packet):
    fields_desc = [ BitField("swid", 0x0, 6),
                  BitField("inport", 0x0, 6),
                  BitField("rule", 0x0, 20)]


    def extract_padding(self, p):
                return "", p


class IVPOption_MRI(IPOption):
    name = "MRI"
    option = 31
    fields_desc = [ _IPOption_HDR,
                    FieldLenField("length", None, fmt="B",
                                  length_of="swtraces",
                                  adjust=lambda pkt,l:l*2+4),
                    ShortField("count", 0),
                    PacketListField("swtraces",
                                   [],
                                   SwitchTrace,
                                   count_from=lambda pkt:(pkt.count*1)) ]


def check_packet(queue):
    while True:
        path = queue.get()
        verif = Verification()
        verif_path = verif.verif_packet(path)


def handle_pkt(pkt, q):
    #pkt.show2()
    global NUM
    count = 0
    path = []
    while (count < pkt['MRI'].count):
        swid = pkt['MRI'].swtraces[count].swid
        inport = pkt['MRI'].swtraces[count].inport
        ruleid = pkt['MRI'].swtraces[count].rule
        dst_ip = pkt['IP'].dst
        path.insert(0, [dst_ip, swid, inport, ruleid])
        count = count + 1
    NUM = NUM + 1
    q.put([path, NUM, len(path)])
    print("Path %i: %s" % (NUM, path))
    sys.stdout.flush()


def main():
    q = Queue.Queue()
    workers = 8

    for i in range(workers):
        thread = Thread(target=check_packet, args=(q, ))
        thread.setDaemon(True)
        thread.start()

    iface = 'enp0s8'
    print 'Path Format [vlanID, [dst_ip, swID, inport, ruleID], ...]\n'
    sys.stdout.flush()
    try:
        sniff(filter='udp', iface = iface, prn = lambda x: handle_pkt(x, q))
    finally:
        for key in redis_session.scan_iter("s*"):
            redis_session.delete(key)


if __name__ == '__main__':
    main()
