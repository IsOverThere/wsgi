from show_status import show_status
from show_status import show_list

url_app_mapping = {
        '/':show_status,
        '/list':show_list
        }


def urlrouting(environ, start_response):
    url = environ['PATH_INFO']
    app = url_app_mapping[url]
    result = app(environ, start_response)
    return result
