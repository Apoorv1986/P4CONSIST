#!/bin/python

class Policy:

    def ip_to_bits(self, n):
        "Convert the IP address to a binary 32-bits list"
        return ''.join([bin(int(x)+256)[3:] for x in n.split('.')])


    def bm(self, var_ip, var_port, width, prefix_ip, prefix_port, var_rule, prefix_rule, var_vlan, prefix_vlan):
        "Binary Matching: IP Address LPM And (InPorts, RuleID, VLAN ID) matching"
        #convert the virtual packets' dst IP address to binay
        var_ip_bits = self.ip_to_bits(var_ip)
        #convert the rule dst IP address to binay
        prefix_ip_bits = self.ip_to_bits(prefix_ip)
        #extract the mask "width" part of the IP addresses
        var_ip_bits = var_ip_bits[0:width]
        prefix_ip_bits = prefix_ip_bits[0:width]

        count = 0
        # check the ingress port, rule and vlan 
        if var_port == prefix_port and var_rule == prefix_rule and var_vlan == prefix_vlan:
            #Apply the LPM where "width" is the mask    
            while (count < width):
                if not int(var_ip_bits[count]) ^ int(prefix_ip_bits[count]) == 0:
                    return False
                count = count + 1
            return True
        return False
