import rate_info

url_app_mapping = {
        '/':rate_info.show_current_status,
        '/list':rate_info.show_list
        }


def urlrouting(environ, start_response):
    url = environ['PATH_INFO']
    app = url_app_mapping[url]
    result = app(environ, start_response)
    return result
