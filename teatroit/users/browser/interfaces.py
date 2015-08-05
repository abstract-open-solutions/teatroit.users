from zope.interface import Interface
from zope import schema
from quintagroup.formlib.captcha import Captcha
from zope.app.form.browser.itemswidgets import SelectWidget

from teatroit.site.vocabularies import RegistrySource
from teatroit.site.interfaces.settings import IGlobalCTSettings


from .. import _


SelectWidget._messageNoValue = _(
    "vocabulary-missing-single-value-for-edit",
    "Seleziona un valore."
)


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
    provincia = schema.Choice(
        title=_(u"Provincia"),
        description=u"",
        vocabulary=u'provincia_vocab'
    )


class ITeatroRegistration(Interface):
    location = schema.TextLine(title=_(u"Indirizzo"), description=u"")
    comune = schema.TextLine(title=_(u"Comune"), description=u"")
    provincia = IUtenteRegistration['provincia']
    cap = schema.TextLine(title=_(u"CAP"), description=u"")
    telefono = schema.TextLine(title=_(u"Telefono"), description=u"")


class ICompagniaRegistration(Interface):
    compagnia_tipo = schema.Choice(
        title=_(u"Tipo compagnia"),
        description=u"",
        vocabulary=u'compagnia_tipo_vocab'
    )


class IUtenteRedazioneSchema(Interface):
    redazione_argomento = schema.Choice(
        title=_(u"Ruolo redazione"),
        description=u"",
        source=RegistrySource(
            iface=IGlobalCTSettings,
            fname='issues_options',
        )
    )
    redazione_regione_editoriale = schema.Choice(
        title=_(u"Regione editoriale"),
        description=u"",
        source=RegistrySource(
            iface=IGlobalCTSettings,
            fname='editorial_regions',
            first_item='--',
        ),
    )
