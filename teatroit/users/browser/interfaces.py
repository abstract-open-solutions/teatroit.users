from zope.interface import Interface
from zope import schema
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


class IUtenteRegistration(Interface):
    provincia = schema.TextLine(title=u"provincia", description=u"")


class ITeatroRegistration(Interface):
    location = schema.TextLine(title=u"location", description=u"")
    comune = schema.TextLine(title=u"comune", description=u"")
    provincia = schema.TextLine(title=u"provincia", description=u"")
    cap = schema.TextLine(title=u"cap", description=u"")
    telefono = schema.TextLine(title=u"telefono", description=u"")

class ICompagniaRegistration(Interface):
    tipo = schema.TextLine(title=u"tipo", description=u"")
