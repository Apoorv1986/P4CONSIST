#!/bin/python2.7

import networkx as nx
import json
import glob
import os
import copy
import sys
import time
import redis
import ast

from policy import Policy
from topology import Topology
from datetime import datetime


G = nx.Graph()
topo = Topology()
policy = Policy()
PATHS_CHECK = {}
ruleID_list = []
SOURCE = ""
TARGET = ""
EXPIRE = 10
redis_session = redis.Redis(host='localhost')


class Verification:


    def get_next_port(self, sw, nxt_sw, port):
        "Find the destination port in the link"
        links = topo.get_links()
        for link in links:
            if (sw in link[0] and nxt_sw in link[1]) or (sw in link[1] and nxt_sw in link[0]):
                if str(port) in link[0].split(':')[1]:
                    return int(link[1].split(':')[1])
                elif str(port) in link[1].split(':')[1]:
                    return int(link[0].split(':')[1])


    def verif_paths(self, packet, paths, number):
        "Verify if the given packet can be routed through these paths"
        path_count = 0
        diffTime = 0
        t0 = time.time()
        for path in paths:
            tmp_pkt = copy.copy(packet)
            prv_sw_chk = True
            for index, sw in enumerate(path):
                next = index + 1
                rules = topo.get_switch_rules(sw)
                sw_chk = False
                for rule in rules:
                    rule_chk = False
                    rule_chk = policy.bm(tmp_pkt[0], tmp_pkt[1], rule[1], rule[0], rule[2], tmp_pkt[2], rule[4], tmp_pkt[3], rule[5])
                    if rule_chk:
                        sw_chk = True
                        if next < len(path):
                            tmp_pkt[1] = self.get_next_port(sw, path[next], rule[3])
                            tmp_pkt[2] = ruleID_list[next]
                        break
                prv_sw_chk = sw_chk & prv_sw_chk
                if not prv_sw_chk:
                    break
            PATHS_CHECK[path_count] = prv_sw_chk
            path_count = path_count + 1
        #print PATHS_CHECK
        t1 = time.time()
        diffTime = t1 - t0
        print("Checking time %s: %s" % (number, diffTime))
        return PATHS_CHECK


    def verif_paths_no_cutoff(self, packet, paths, number):
        "Verify if the given packet can be routed through this path"
        path_count = 0
        diffTime = 0
        t0 = time.time()
        for path in paths:
            tmp_pkt = copy.copy(packet)
            prv_sw_chk = True
            for index, sw in enumerate(path):
                next = index + 1
                rules = topo.get_switch_rules(sw)
                sw_chk = False
                for rule in rules:
                    rule_chk = False
                    rule_chk = policy.bm(tmp_pkt[0], tmp_pkt[1], rule[1], rule[0], rule[2], tmp_pkt[2], rule[4], tmp_pkt[3], rule[5])
                    if rule_chk:
                        sw_chk = True
                        if next < len(path):
                            tmp_pkt[1] = self.get_next_port(sw, path[next], rule[3])
                            tmp_pkt[2] = ruleID_list[next]
                        break
                prv_sw_chk = sw_chk & prv_sw_chk
                if not prv_sw_chk:
                    break
            PATHS_CHECK[path_count] = prv_sw_chk
            path_count = path_count + 1
        #print PATHS_CHECK
        t1 = time.time()
        diffTime = t1 - t0
        print("Checking time without cutoff %s: %s" % (number, diffTime))
        return PATHS_CHECK


    def verif_packet(self, path_to_check):
        cutoff = path_to_check[2]
        number = path_to_check[1]  #order of the packet
        vlanid = path_to_check[3]

        topo.set_graph(G)
        topo.create_graph()
        SOURCE = 's' + str(path_to_check[0][0][1])
        TARGET = 's' + str(path_to_check[0][cutoff-1][1])
        path_to_check = path_to_check[0]

        paths = []
        paths2 = [] #Add an 's' to switch names

        del ruleID_list[:]

        for sw in path_to_check:
            sw[1] = 's' + str(sw[1])
            paths2.append(sw[1])
            ruleID_list.append(sw[3])

        paths = redis_session.get(str(vlanid) + '_' + SOURCE + '_' + TARGET)
        PATHS_CHECK = redis_session.get(str(vlanid) + '_' + SOURCE + '_' + TARGET + '_check')

        if paths and PATHS_CHECK:
            PATHS_CHECK = ast.literal_eval(PATHS_CHECK)
            paths = ast.literal_eval(paths)
        else:
            print '++++++++++ not found in memory! ++++++++++++'
            packet = [path_to_check[0][0], path_to_check[0][2], path_to_check[0][3], vlanid]
            
            paths = topo.get_paths(G, SOURCE, TARGET, cutoff, number)
            #paths = topo.get_paths_no_cutoff(G, SOURCE, TARGET, number)
            PATHS_CHECK = self.verif_paths(packet, paths, number)
            #PATHS_CHECK = self.verif_paths_no_cutoff(packet, paths, number)

            redis_session.set(str(vlanid) + '_' + SOURCE + '_' + TARGET, str(paths))
            redis_session.expire(str(vlanid) + '_' + SOURCE + '_' + TARGET, EXPIRE)

            redis_session.set(str(vlanid) + '_' + SOURCE + '_' + TARGET + '_check', str(PATHS_CHECK))
            redis_session.expire(str(vlanid) + '_' + SOURCE + '_' + TARGET + '_check', EXPIRE)

        #print('\nPossible paths: %s' % paths)
        #print("Total number of paths: %i\n" % len(paths))
        #print ('PATHS_CHECK: %s' % PATHS_CHECK)

        try:
            found = paths.index(paths2)
        except ValueError:
            print 'The packet took a new path uncovered by the list of possible paths!'
            sys.exit(1)

        tim = 0

        if PATHS_CHECK[found]:
            print("Packet %i vlan %i ------> Consistent!" % (number, vlanid))

        else:
            tim = datetime.now().strftime("%M:%S.%f")
            print("Packet %i vlan %i ------> Inconsistent!=%s\n" % (number, vlanid, tim))

