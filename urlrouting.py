import rate_info

url_app_mapping = {
        '/':rate_info.current_status,
        '/list.wsgi':rate_info.list
        }

def page_not_found(environ, start_response):
    output = 'Page Not Found'
    status = '404 Page Not Found'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return output 


def urlrouting(environ, start_response):
    url = environ['PATH_INFO']
    try:
        app = url_app_mapping[url]
        result = app(environ, start_response)
    except KeyError:
        result = page_not_found(environ, start_response)
    return result

