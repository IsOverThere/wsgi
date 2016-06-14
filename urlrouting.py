import show_status

url_app_mapping = {
        '/':show_status.show_status
        }


def urlrouting(environ, start_response):
    url = environ['PATH_INFO']
    app = url_app_mapping[url]
    result = app(environ, start_response)
    return result
