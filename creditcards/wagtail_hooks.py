from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from .models import CreditCard, CardIssuer


class CreditCardAdmin(ModelAdmin):
    model = CreditCard
    menu_label = 'Cards'
    menu_icon = 'form'  # change as required
    list_display = ('name', 'issuer', 'processing_network', 'slug', 'modified')


class CardIssuerAdmin(ModelAdmin):
    model = CardIssuer
    menu_icon = 'form'  # change as required
    list_display = ('name', 'cj_advertiser_id')


class CreditCardReviews(ModelAdminGroup):
    menu_label = 'Credit Cards'
    menu_icon = 'folder-open-inverse'
    items = (CreditCardAdmin, CardIssuerAdmin)

modeladmin_register(CreditCardReviews)
