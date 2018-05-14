import uuid
from django import forms
from django.db.models import UUIDField
from wagtail.wagtailcore import models, fields, blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from hydra_client import CreateContentRequest

from www.page_types.articles import ALLOWED_SERVICES
from pages.custom_edit_handlers import ReadOnlyPanel


class HeadingBlock(blocks.CharBlock):

    @property
    def media(self):
        return forms.Media(
            css={
                'screen': ('about/css/blocks/heading.css', )
            }
        )

    class Meta:
        template = 'about/blocks/heading.html'
        icon = 'title'


class AwardBlock(blocks.StructBlock):
    badge = ImageChooserBlock()

    class Meta:
        template = 'about/blocks/award.html'


class AboutPage(models.Page):
    uuid = UUIDField(editable=False, default=uuid.uuid4)  # Hydra needs uuids

    body = fields.StreamField([
        ('banner', ImageChooserBlock()),
        ('heading', HeadingBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('video', EmbedBlock()),
        ('awards', blocks.ListBlock(AwardBlock(label="awards"), template='about/blocks/awards_list.html'))
    ])

    def create_hydra_content(self):
        cr = CreateContentRequest(
            headline=self.title,
            body=self.body.render_as_block(),
            product_id=ALLOWED_SERVICES.usmf.value,
            url=self.url,
            publish_at=self.first_published_at,
            uuid=str(self.uuid),
            visibility=100,  # 100 is publish
            is_static=True,  # Don't include in aggregators
        )
        # Hydra requires first and last name but does its own look up and ignores these values.
        cr.set_primary_author(1589, 'Motley', 'Fool Staff')
        return cr

    content_panels = models.Page.content_panels + [
        StreamFieldPanel('body'),
        ReadOnlyPanel('uuid', heading='Page UUID'),
    ]
