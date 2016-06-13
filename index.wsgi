import os, sys
sys.path.append(os.path.dirname(__file__))
import web_get_ss_log_now

def application(environ, start_response):
    """Simplest possible application object"""
    #output = "hello world"
    output = web_get_ss_log_now.web_get_ss_log_now()
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [output] #Must with []
