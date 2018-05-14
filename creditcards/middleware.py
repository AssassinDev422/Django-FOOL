from premium_skinner import middleware


class PremiumIdMiddleware(middleware.PremiumIdMiddleware):
    ''' Used instead of the Premium Skinner equivalent for compatibility with Wagtail'''

    def process_request(self, request):
        request.premium_id = None

    def process_view(self, request, view_func, view_args, view_kwargs):
        request.premium_id = request.GET.get('premium', None) or view_kwargs.get('premium', None)
