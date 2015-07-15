from zope.interface import Interface
from quintagroup.formlib.captcha import Captcha
from .. import teatroitUsersMessageFactory as _


class IBasicRegistrationForm(Interface):
    """Marker interface for my custom registration form
    """


class ICaptchaSchema(Interface):
    captcha = Captcha(
        title=_(u'Verification'),
        description=_(
            u'Type the code from the picture shown below.'
        ),
    )
