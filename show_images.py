#!/usr/bin/env python
import StringIO
import os

def images_data(environ, start_response):
    ext = environ['PATH_INFO'].split('.')
    for n in ext:
        mime = n
    response_headers = [('Content-type', 'image/'+mime)]
    status = '200 OK'
    start_response(status, response_headers)
    #image = open(os.getcwd()+environ['PATH_INFO'], "rb")
    try:
        image = open('/var/www/python/images'+environ['PATH_INFO'], "rb")
    except IOError: 
        image = open('/var/www/python/images/404.jpg', "rb")

    strio = StringIO.StringIO(image.read()).getvalue()
    return strio
