#!/usr/bin/env python
import commands
 
def show_current_status(environ, start_response):
    status, output = commands.getstatusoutput('cat /tmp/iptables_now.log')
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return output 

def show_list(environ, start_response):
    status, output = commands.getstatusoutput('ls /var/log/iptables.log|sort')
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return output 
