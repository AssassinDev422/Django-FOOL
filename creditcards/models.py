from HTMLParser import HTMLParser
from django.db import models
from django.http import Http404
from django.utils.text import slugify
from django.utils.functional import cached_property
from django.utils.encoding import python_2_unicode_compatible
from django.core import files
from logging import getLogger
import requests
from PIL import Image
from io import BytesIO
from model_utils.models import TimeStampedModel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.url_routing import RouteResult
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, InlinePanel, StreamFieldPanel
)
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.contrib.table_block.blocks import TableBlock
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from tstr.views.dispatch import dispatcher as tstr_view

from creditcards import conf
from creditcards.disclosure import disclosure_generator

html_parser = HTMLParser()
logger = getLogger(__name__)

class TstrHanlderPage(Page):
    def route(self, request, path_components):
        try:
            return super(TstrHanlderPage, self).route(request, path_components)
        except Http404:
            return RouteResult(self)

    def serve(self, request):
        return tstr_view(request)


class CardIssuer(TimeStampedModel):
    name = models.CharField(max_length=200, blank=False, unique=True)
    possessive_name = models.CharField(max_length=200, blank=False)
    cj_advertiser_id = models.IntegerField(unique=True, null=True, blank=True)
    requires_intermediate_page = models.BooleanField(default=False)
    show_fee_link = models.BooleanField(
        help_text='Show detailed rates and fees link for this card issuer',
        default=True
    )

    def __unicode__(self):
        return self.name

@register_snippet
class CreditCard(TimeStampedModel):
    PROCESSING_NETWORKS = conf.PROCESSING_NETWORKS
    name = models.CharField(max_length=200, blank=False, unique=True)
    slug = models.SlugField(max_length=200, unique=True, editable=False)
    marketing_copy = RichTextField(blank=True)
    intro_purchase_apr = models.TextField(blank=True)
    purchase_apr = models.TextField(blank=True)
    intro_transfer_apr = models.TextField(blank=True)
    transfer_apr = models.TextField(blank=True)
    credit_rating = models.TextField(blank=True)
    annual_fee = models.TextField(blank=True)
    application_link = models.URLField(blank=True)
    detailed_rates_and_fees_link = models.URLField(blank=True)
    issuer = models.ForeignKey(CardIssuer, null=True)
    processing_network = models.IntegerField(choices=PROCESSING_NETWORKS, null=True)
    rewards_bonus = models.TextField(blank=True)
    rewards_bonus_terms = models.TextField(blank=True)
    image = models.ImageField(upload_to='credit-card-art', null=True)
    # Fields required for Capital One credit offers API
    card_type_choices = (
        ('business', 'Business Card'),
        ('consumer', 'Consumer Card'),
    )
    product_id = models.CharField(
        max_length=200, blank=True,
        help_text='Required only if card Issuer is Capital One'
    )
    card_type = models.CharField(
        max_length=10, blank=True, choices=card_type_choices,
        help_text='Required only if card Issuer is Capital One'
    )

    def save(self, *args, **kwargs):
        self.name, self.slug = CreditCard.get_name_and_slug(self.name)
        super(CreditCard, self).save(*args, **kwargs)

    def update_image(self, image_source_url):
        try:
            response = requests.get(image_source_url, stream=True)
            if response.status_code == requests.codes.ok:
                image_file = BytesIO(response.content)
                image = Image.open(image_file)
                self.image.save('{0}.{1}'.format(self.slug, image.format.lower()), files.File(image_file))
                self.save(update_fields=['image'])
        except:
            logger.error('Image upload failed for %s: image: %s', self.name, image_source_url)

    @staticmethod
    def get_name_and_slug(name):
        name = html_parser.unescape(name)
        slug = slugify(name.encode('ascii', 'ignore'))
        return name, slug

    def conduit_link(self):
        if self.review:
            return self.review.conduit_url
        return ''

    @cached_property
    def conduit_required(self):
        return self.issuer.requires_intermediate_page

    def __unicode__(self):
        return self.name


class CreditCardIndex(Page):
    '''
    The home page for the credit card section.
    '''
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    subpage_types = [
        'creditcards.CreditCardReview',
        'creditcards.CreditCardList',
    ]

class CreditCardReviewTag(TaggedItemBase):
    '''
    Tags for credit card reviews.
    '''
    content_object = ParentalKey('creditcards.CreditCardReview', related_name='tagged_items')


class CreditCardReview(RoutablePageMixin, Page):
    '''
    The review of a card. Includes both the summary and the full review.
    Inherits from Page because it generates a page on the site.
    '''
    card = models.OneToOneField(CreditCard, related_name='review', on_delete=models.PROTECT)
    intro = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('blockquote', blocks.BlockQuoteBlock()),
        ('table_block', TableBlock()),
    ], blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('blockquote', blocks.BlockQuoteBlock()),
        ('table_block', TableBlock()),
    ])
    pros = RichTextField(default='<ul><li></li></ul>')
    cons = RichTextField(default='<ul><li></li></ul>')
    tags = ClusterTaggableManager(through=CreditCardReviewTag, blank=True)

    content_panels = Page.content_panels + [
        SnippetChooserPanel('card'),
        #FieldPanel('card', classname="full"),
        StreamFieldPanel('intro'),
        StreamFieldPanel('body'),
        FieldPanel('pros', classname="full"),
        FieldPanel('cons', classname="full"),
        FieldPanel('tags', classname="full"),
    ]

    @route(r'^card/$', name='conduit')
    def conduit(self, request):
        self.template = 'creditcards/credit_card_only.html'
        self.conduit = True
        return self.serve(request)

    @route(r'^$') #need default for revision view it seems
    def regular(self, request):
        return self.serve(request)

    @cached_property
    def conduit_url(self):
        subpage_url = self.reverse_subpage('conduit')
        if not self.url.endswith('/') and not subpage_url.startswith('/'):
            return self.url + '/' + subpage_url
        return self.url + subpage_url

    parent_page_types = ['creditcards.CreditCardIndex']

    def disclosure(self):
        return disclosure_generator(self.card.processing_network)


class CreditCardList(Page):
    '''
    An editorial list of credit cards.
    '''
    body = RichTextField()
    ending = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('table_block', TableBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        InlinePanel('items', label="Cards"),
        StreamFieldPanel('ending'),
    ]

    parent_page_types = ['creditcards.CreditCardIndex']

    def disclosure(self):
        #drafts don't work with values_list becuase they are a modelcluster
        networks = (item.card.processing_network for item in self.items.all())
        return disclosure_generator(*networks)


class CreditCardListItem(Orderable):
    '''
    Each item in the CreditCardList.
    '''
    page = ParentalKey(CreditCardList, related_name='items')
    card = models.ForeignKey(CreditCard, related_name='card_list_items')
    summary = RichTextField()
    subhead = models.CharField(max_length=255, blank=True, help_text=("Optional subhead for grouping cards on the page"))


    panels = [
        FieldPanel('subhead'),
        FieldPanel('card'),
        FieldPanel('summary'),
    ]


@register_snippet
@python_2_unicode_compatible
class CreditCardListPageSidebarLink(models.Model):
    categories = (
        ('type', 'Type'),
        ('issuer', 'Issuer'),
        ('creditscore', 'Credit Score'),
    )
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)
    categorized_by = models.CharField(max_length=255, choices=categories)

    panels = [
        FieldPanel('url'),
        FieldPanel('text'),
        FieldPanel('categorized_by'),
    ]

    def __str__(self):
        return self.text
