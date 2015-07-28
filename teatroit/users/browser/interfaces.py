from zope.interface import Interface
from zope import schema
from quintagroup.formlib.captcha import Captcha
from zope.app.form.browser.itemswidgets import SelectWidget
from .. import teatroitUsersMessageFactory as _


SelectWidget._messageNoValue = _("vocabulary-missing-single-value-for-edit",
                      "Seleziona un valore.")


class IBasicRegistrationForm(Interface):
    """Marker interface for my custom registration form
    """


class ICaptchaSchema(Interface):
    captcha = Captcha(
        title=_(u'Verifica'),
        description=_(
            u'Digita il codice mostrato nell\'immagine.'
        ),
    )


class IUtenteRegistration(Interface):
    provincia = schema.Choice(title=_(u"Provincia"), description=u"",
                              vocabulary=u'provincia_vocab')


class ITeatroRegistration(Interface):
    location = schema.TextLine(title=_(u"Indirizzo"), description=u"")
    comune = schema.TextLine(title=_(u"Comune"), description=u"")
    provincia = IUtenteRegistration['provincia']
    cap = schema.TextLine(title=_(u"CAP"), description=u"")
    telefono = schema.TextLine(title=_(u"Telefono"), description=u"")

class ICompagniaRegistration(Interface):
    compagnia_tipo = schema.Choice(title=_(u"Tipo compagnia"), description=u"",
                         vocabulary=u'compagnia_tipo_vocab')
