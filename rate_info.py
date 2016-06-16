#!/usr/bin/env python
import commands
import re
style = """
<style type="text/css">
a:link {
    font-size: 10pt;
    color: #006699;
    font-family: Calibri;
    text-align: left;
    text-decoration: none;
}
a:visited {
    font-size: 10pt;
    color: #990066;
    font-family: Calibri;
    text-align: left;
    text-decoration: none;
}
a:hover {
    font-size: 10pt;
    color: #cccc33;
    font-family: Calibri;
    text-align: left;
    text-decoration: underline;
}
a:active {
    font-size: 10pt;
    color: #ff6666;
    font-family: Calibri;
    text-align: left;
    text-decoration: underline;
}
</style>

"""

html = """ 
<html>
    <head>
    %s
    </head>
    <body>
    %s
    </body>
</html>
"""
 

def current_status(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)

    status, output = commands.getstatusoutput('cat /tmp/iptables_now.log')
    return output 


def get_log_list_html():
    status, list = commands.getstatusoutput('ls /var/log/iptables.log')
    list = list.split()
    body=''
    for line in list:
        body = body+'\t<a href="list.wsgi?file='+line+'">'+line+'</a><br>\n'
    output=html%(style, body)
    return output


def get_log_list(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)

    output=get_log_list_html()
    return output 


def get_one_log_html(environ):
    query_string = environ['QUERY_STRING']
    fileMatch = re.match('^file=(.*)$', query_string, re.M|re.I)
    if fileMatch:
        logfile = fileMatch.group(1)
    else:
        output="No file matched"
    logfile = '/var/log/iptables.log/'+logfile
    status, output = commands.getstatusoutput('cat ' + logfile )
    return output 


def get_one_log(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)

    output = get_one_log_html(environ)
    return output 


def list(environ, start_response):
    query_string = environ['QUERY_STRING']
    if query_string == '':
        output = get_log_list(environ, start_response)
    else:
        output = get_one_log(environ, start_response)
    return output 

#status, output = commands.getstatusoutput('ls /var/log/iptables.log|sort')
#status = '200 OK'
#response_headers = [('Content-type', 'text/plain')]
#start_response(status, response_headers)
#return output 

if __name__ == '__main__':
    output=get_log_list_html()
    status, output = commands.getstatusoutput('echo "' + output + '" > /home/zhangcl/test.htm')
