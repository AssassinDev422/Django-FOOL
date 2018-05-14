import inflect

from creditcards.conf import PROCESSING_NETWORKS

i = inflect.engine()

def disclosure_generator(*networks):
    def process_names(networks):
        return [PROCESSING_NETWORKS[idx] for idx in networks]

    networks = set(networks)
    own_and_rec = set([PROCESSING_NETWORKS.mastercard, PROCESSING_NETWORKS.visa])
    rec_only = set([PROCESSING_NETWORKS.amex])

    owned = networks & own_and_rec
    reced = networks & rec_only
    msgs = []
    if owned:
        msg = u'The Motley Fool owns shares of and recommends {}.'.format(i.join(process_names(owned)))
        msgs.append(msg)

    if reced:
        msg = u'The Motley Fool recommends {}.'.format(i.join(process_names(reced)))
        msgs.append(msg)

    if not any(owned | reced):
        msg = 'The Motley Fool has no position in any of the stocks mentioned.'
        msgs.append(msg)
    return ' '.join(msgs)
