import os, sys
sys.path.append(os.path.dirname(__file__))
import urlrouting

def application(environ, start_response):
    """Simplest possible application object"""
    result = urlrouting.urlrouting(environ, start_response)
    return [result]

#def application(environ, start_response):
#    """Simplest possible application object"""
#    output = "hello world"
#    status = '200 OK'
#    response_headers = [('Content-type', 'text/plain')]
#    start_response(status, response_headers)
#    return [output] #Must with []
