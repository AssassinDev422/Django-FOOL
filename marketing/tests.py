from django.core.urlresolvers import reverse
from django.test import TestCase

class InvisiblePixelTests(TestCase):

    def test_view_returns_gif(self):
        url = reverse('get_tracking_pixel')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'GIF89a\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;')

    def test_view_returns_visitor_cookie_if_uid_in_query_string(self):
        url = reverse('get_tracking_pixel') + "?uid=5"
        response = self.client.get(url)
        self.assertIsNotNone(response.cookies['Visitor'])
        self.assertTrue('uid=5' in response.cookies['Visitor'].value.split('&'))
