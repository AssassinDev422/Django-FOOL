from django.http import HttpResponse
from fool_cookies.middleware import VisitorCookieMiddleware

PIXEL_GIF_DATA = """
\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b
""".strip()


class MarketingVisitorCookieMiddleware(VisitorCookieMiddleware):

    def __init__(self, fool_uid):
        super(MarketingVisitorCookieMiddleware, self).__init__()
        self.fool_uid = fool_uid

    def get_fool_uid(self, request,response):
        return self.fool_uid

    def apply_cookie(self, request, response):
        response.set_cookie(key=self.get_cookie_name(), value=self.get_cookie_value(request, response),
            expires=self.get_cookie_expiration(), secure=False,
            path='/', domain='.fool.com', )


def get_tracking_pixel(request):
    response =  HttpResponse(PIXEL_GIF_DATA, content_type='image/gif')

    user_id = request.GET.get('uid') or request.GET.get('u')
    if user_id and not request.user.is_authenticated():
        try:
            user_id = int(user_id)
            marketing_visitor_cookie_middleware = MarketingVisitorCookieMiddleware(user_id)
            if not request.COOKIES.get(marketing_visitor_cookie_middleware.get_cookie_name()):
                marketing_visitor_cookie_middleware.apply_cookie(request, response)
        except:
            pass

    return response
