#!/usr/bin/env python
import commands
 
def get_iptables_status():
    status, output = commands.getstatusoutput('iptables -L -nv')
    return output
 
if __name__ == '__main__':
    output = get_iptables_status()
    print output
