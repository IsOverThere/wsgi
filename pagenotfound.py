#!/usr/bin/env python
import os, sys
import commands

html = """ 
<html>
    <body>
    <table width="100%" border="0">
        <tr>
            <td align="center">
            <font size="15" face="Source Sans Pro Black">Oops...404 not found!</font>
            </td>
        </tr>
        <tr>
            <td align="center">
            <img src="404.jpg" />
            </td>
        </tr>
    </table>
    </body>
</html>
"""

def pagenotfound_html():
    output=html
    return output

def show_pagenotfound(environ, start_response):
    status = '404 Page Not Found'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    output = pagenotfound_html()
    return output 

if __name__ == '__main__':
    output=pagenotfound_html()
    status, output = commands.getstatusoutput('echo "' + output + '" > /home/zhangcl/test.htm')
