from django.conf.urls import patterns, url
from views import get_tracking_pixel

urlpatterns = patterns('',
    url(r'^foolcookie.ashx$', get_tracking_pixel, name='get_tracking_pixel'),
    url(r'^fool-cookies$', get_tracking_pixel, name='get_tracking_pixel'),
)
