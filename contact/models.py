from modelcluster.fields import ParentalKey

from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
)
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailforms.edit_handlers import FormSubmissionsPanel
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailadmin.utils import send_mail


class ContactFormField(AbstractFormField):
    page = ParentalKey('ContactPage', related_name='contact_fields')


class ContactPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('blockquote', blocks.BlockQuoteBlock()),
        ('raw_html', blocks.RawHTMLBlock()),
    ], blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro', classname="full"),
        InlinePanel('contact_fields', label="Form fields"),
        StreamFieldPanel('body'),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def get_form_fields(self):
        return self.contact_fields.all()

    def send_mail(self, form):
        # Overwrite the send_mail method from AbstractEmailForm
        # to use inquiry as email subject.
        addresses = [x.strip() for x in self.to_address.split(',')]
        content = []
        subj = None
        send_from = self.from_address
        for field in form:
            if 'inquiry' in field.name:
                subj = field.value()
            elif 'email' in field.name.lower():
                send_from = field.value()
            value = field.value()
            if isinstance(value, list):
                value = ', '.join(value)
            content.append('{}: {}'.format(field.label, value))
        content = '\n'.join(content)
        if subj:
            send_mail(subj, content, addresses, send_from,)
        else:
            send_mail(self.subject, content, addresses, send_from,)
