import os, sys
sys.path.append(os.path.dirname(__file__))
#sys.path.append(os.path.dirname(__file__))
import get_iptables_status
#def get_iptables_status():
#    status, output = commands.getstatusoutput('ls -als')
#    #status, output = commands.getstatusoutput('iptables -L -nv')
#    return output

def application(environ, start_response):
    """Simplest possible application object"""
    output = get_iptables_status.get_iptables_status()
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [output] #Must with []
