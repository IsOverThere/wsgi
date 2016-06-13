#!/usr/bin/env python
import commands
 
def web_get_ss_log_now():
    status, output = commands.getstatusoutput('cat /tmp/iptables_now.log')
    return output
 
if __name__ == '__main__':
    output = web_get_ss_log_now()
    print output
