from django.utils.translation import ugettext_lazy as _

CONDITION_CHIOICE = (
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