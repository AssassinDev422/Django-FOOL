from django import template

from tstr.models import Route

register = template.Library()

@register.inclusion_tag('dashboard/partials/_active_tests.html')
def active_tests():
    all_routes = Route.objects.all().order_by('name')
    context = {}
    context['all_routes'] = all_routes
    return context

@register.simple_tag()
def is_test_active_color(route, test):
    return "green" if route.is_segment_test_active(test) else "grey"
