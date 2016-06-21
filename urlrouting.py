import rate_info
import pagenotfound
import show_images

url_app_mapping = {
        '/now.wsgi':rate_info.current_status,
        '/list.wsgi':rate_info.list
        }


def urlrouting(environ, start_response):
    url = environ['PATH_INFO']
    if '.jpg' in url or '.png' in url:
        result = show_images.images_data(environ, start_response)
    else:
        try:
            app = url_app_mapping[url]
            result = app(environ, start_response)
        except KeyError:
            result = pagenotfound.show_pagenotfound(environ, start_response)
    return result

