from django.utils.translation import ugettext_lazy as _

CONDITION_CHOICE = (
    ('Present Condition', _('Present Condition')),
    ('Future Condition', _('Future Condition')),
    ('Management Measures',_('Management Measures')),
)

PRESSURE_TYPE_CHOICE = (
    ('main', _('Main Pressure')),
    ('bg', _('Background Pressure')),
)

USE_TYPE_CHOICE = (
    ('main', _('Main Use')),
    ('sec', _('Secondary Use')),
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