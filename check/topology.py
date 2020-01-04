#!/bin/python2.7

import networkx as nx
import json
import glob
import csv
import policy
import os
import time

SWITCHES = []
switch_rules = {}
PATHS = []
TOPOLOGY_FILES = '/vagrant/runtimes_15000/'
LINKS_FILE = TOPOLOGY_FILES + 'links.csv'
LINKS = []
GRAPH = None


class Topology:
    def parse_json(self):
        "Parse the switches' runtime files into a dictionary"
        for file in glob.glob(TOPOLOGY_FILES + '*.json'):

            with open(file, 'r') as f:
                data = json.load(f)

            table = data['table_entries']
            rules_list = []
            for rule in table:
                list = []
                #Extract the switch ID from the default action
                if(rule.get('default_action')):
                    switch_name = 's' + str(rule['action_params']['swid'])
                    SWITCHES.append(switch_name)
                #Extract of the rules data
                if(rule.get('match')):
                    ip = rule['match']['hdr.ipv4.dstAddr'][0]
                    mask = rule['match']['hdr.ipv4.dstAddr'][1]
                    inPort = rule['match']['standard_metadata.ingress_port']
                    vlanid = rule['match']['hdr.dot12q.vlan']
                    dstAddr = rule['action_params']['dstAddr']
                    outPort = rule['action_params']['port']
                    ruleID = rule['action_params']['rule']
                    #Save the rule data as a list
                    list = [ip, mask, inPort, outPort, ruleID, vlanid]
                    #Append the rule to the list of rules
                    rules_list.append(list)
            #Save the rules as dictionary / Key: switchID, Value: list of all rules
            switch_rules[switch_name] = rules_list


    def parse_links(self):
        "Parse the links file"
        with open(LINKS_FILE) as file:
            reader = csv.reader(file, delimiter=',')
            for link in reader:
                if link:
                    LINKS.append(link)
        return LINKS


    def create_graph(self):
        "Create a Graph"
        global GRAPH
        #Parse the switches' rules
        self.parse_json()
        #Add the switch IDs as nodes in the Graph
        GRAPH.add_nodes_from(SWITCHES)
        #parse the links
        self.parse_links()
        for link in LINKS:
            src_sw = link[0].split(":")[0]
            dst_sw = link[1].split(":")[0]
            GRAPH.add_edge(src_sw, dst_sw)
        return GRAPH


    def get_paths(self, graph, s, t, len, number):
        "find all paths between source and target!"
        paths = []
        #diffTime = 0
        #t0 = time.time()
        paths = nx.all_simple_paths(graph, source=s, target=t, cutoff=len)
        #t1 = time.time()
        #diffTime = t1 - t0
        #print("Graph traversal time %s: %s" % (number, diffTime))
        return list(paths)


    def get_paths_no_cutoff(self, graph, s, t, number):
        "find all paths between source and target without path length cutoff!"
        paths = []
        #diffTime = 0
        #t0 = time.time()
        paths = nx.all_simple_paths(graph, source=s, target=t)
        #t1 = time.time()
        #diffTime = t1 - t0
        #print("Graph traversal time without cutoff %s: %s" % (number, diffTime))
        return list(paths)


    def get_links(self):
        "return a list of all the links in the Graph"
        return LINKS


    def get_switches(self):
        "return a list of all switches/nodes in the Graph"
        return SWITCHES


    def get_switches_rules(self):
        "return a list of all switches' rules"
        return switch_rules


    def get_switch_rules(self, sw):
        "return the rules of the switch sw"
        return switch_rules[sw]


    def set_graph(self, G):
        "sets G as the global GRAPH"
        global GRAPH
        GRAPH = G


    def get_graph(self):
        return GRAPH
