from model_utils.choices import Choices

PROCESSING_NETWORKS = Choices(
    (1, 'visa', 'Visa'),
    (2, 'mastercard', 'MasterCard'),
    (3, 'amex', 'American Express'),
    (4, 'discover', 'Discover'),
)
