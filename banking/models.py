from django.db import models
from django.http import Http404
from django.utils.safestring import mark_safe

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.url_routing import RouteResult
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, InlinePanel, StreamFieldPanel
)
from wagtail.wagtailcore.blocks import StructBlock, StaticBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock

from modelcluster.fields import ParentalKey

from tstr.views.dispatch import dispatcher as tstr_view


banking_table_options = {
    'minSpareRows': 0,
    'startRows': 3,
    'startCols': 3,
    'colHeaders': False,
    'rowHeaders': False,
    'contextMenu': True,
    'editor': 'text',
    'stretchH': 'all',
    'height': 216,
    'language': 'en',
    'renderer': 'html',
    'autoColumnSize': False,
}


class BankingIndexPage(Page):

    subpage_types = [
        'banking.BankingPage',
        'banking.BankingStreamFieldPage',
    ]

    def route(self, request, path_components):
        try:
            return super(BankingIndexPage, self).route(
                request, path_components)
        except Http404:
            return RouteResult(self)

    def serve(self, request):
        return tstr_view(request)

    class Meta:
        verbose_name = 'Banking and Savings index page'


class BankingPage(Page):
    intro_text = RichTextField()
    embed_js = StreamField([
        ('embed_js', blocks.RawHTMLBlock()),
    ])
    closing_text = RichTextField()

    parent_page_types = ['banking.BankingIndexPage']

    content_panels = Page.content_panels + [
        FieldPanel('intro_text', classname='full'),
        StreamFieldPanel('embed_js'),
        InlinePanel('comparison_links', label="Comparison links"),
        FieldPanel('closing_text', classname='full'),
    ]

    class Meta:
        verbose_name = 'Banking and Savings page'


class BankrateWidgetBlock(StaticBlock):
    class Meta:
        icon = "form"
        admin_text = mark_safe('<b>Bankrate Savings/MMA Rates</b>: no configuration needed. Tracking parameters assigned server side.')
        template = "banking/blocks/bankrate_savings_widget.html"
        label = "Savings/MMA Rates"


class BankrateCDRatesBlock(StaticBlock):
    class Meta:
        icon = "form"
        admin_text = mark_safe('<b>Bankrate CD Rates</b>: no configuration needed. Tracking parameters assigned server side.')
        template = "banking/blocks/bankrate_cd_widget.html"
        label = "CD Rates"


class BankrateMortgageRatesBlock(StaticBlock):
    class Meta:
        icon = "form"
        admin_text = mark_safe('<b>Bankrate Mortgage Rates</b>: no configuration needed. Tracking parameters assigned server side.')
        template = "banking/blocks/bankrate_mortgage_widget.html"
        label = "Mortgage Rates"


class BankingComparisonBlock(StructBlock):
    title = blocks.CharBlock()
    body = blocks.RichTextBlock()
    url = blocks.URLBlock()
    image = ImageChooserBlock()

    class Meta:
        icon = "form"
        template = "banking/blocks/banking_comparison.html"
        label = "Banking Comparison Block"


class BankingStreamFieldPage(Page):
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('bankrate_widget', BankrateWidgetBlock()),
        ('bankrate_cd_widget', BankrateCDRatesBlock()),
        ('bankrate_mortgage_widget', BankrateMortgageRatesBlock()),
        ('table_block', TableBlock(table_options=banking_table_options)),
    ])

    comparisons = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('banking_comparison', BankingComparisonBlock()),
        ('bankrate_widget', BankrateWidgetBlock()),
        ('bankrate_cd_widget', BankrateCDRatesBlock()),
        ('bankrate_mortgage_widget', BankrateMortgageRatesBlock()),
        ('table_block', TableBlock(table_options=banking_table_options)),
    ],null=True,blank=True)

    parent_page_types = ['banking.BankingIndexPage']

    class Meta:
        verbose_name = 'Banking and Savings Streamfield page'

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        StreamFieldPanel('comparisons'),
    ]

class BankingPageComparisonLinks(Orderable):
    page = ParentalKey(BankingPage, related_name='comparison_links')
    title = models.CharField(max_length=255)
    body = RichTextField()
    url = models.URLField()
    image = models.ForeignKey(
        'pages.ExtendedImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('body'),
        FieldPanel('url'),
        ImageChooserPanel('image'),
    ]
