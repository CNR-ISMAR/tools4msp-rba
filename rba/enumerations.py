from django.utils.translation import ugettext_lazy as _

CONDITION_CHOICE = (
    ('Present Condition', _('Present Condition')),
    ('Future Condition', _('Future Condition')),
    ('Management Measures',_('Management Measures')),
)

FS_TYPE_CHOICE = (
    ('BG', ('Blue Economy driven')),
    ('CC', _('Climate Change or Conservation driven')),
)

RELEVANCE_TYPE_CHOICE = (
    ('L', _('L ')),
    ('M', _('M')),
    ('H', _('H')),
)


ES_TYPE_CHOICE =(
    ('Habitat Maintenance', _('Habitat Maintenance')),
    ('Carbon Sequestration', _('Carbon Sequestration')),
    ('Food provision', _('Food provision')),
    ('Water Quality', _('Water Quality')),
    ('Fish Migration Route', _('Fish Migration Route')),
    ('Buffering Against Anoxia', _('Buffering Against Anoxia')),
    ('Recreation and Tourism', _('Recreation and Tourism')),
    ('Climate Regulation', _('Climate Regulation')),
)

ES_TYPE_CHOICE =(
    
    ('Provisioning services', _('Provisioning services')),
    ('Regulating and Maintenance Services', _('Regulating and Maintenance Services')),
    ('Cultural Services', _('Cultural Services')),
)

BIO_TYPE_CHOICE =(
    
    ('Biotic', _('Biotic')),
    ('Abiotic', _('Abiotic')),
)