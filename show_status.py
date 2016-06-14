#!/usr/bin/env python
import web_get_ss_log_now
 
def show_status(environ, start_response):
    output = web_get_ss_log_now.web_get_ss_log_now()
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return output 
