from zope.interface import implements
from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema
from .browser.interfaces import (
    IUtenteRegistration,
    ITeatroRegistration,
    ICompagniaRegistration,
    IUtenteRedazioneSchema,
)


class IEnhancedUserDataSchema(IUserDataSchema,
                              ITeatroRegistration,
                              IUtenteRegistration,
                              ICompagniaRegistration,
                              IUtenteRedazioneSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """


class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self): # noqa
        """
        """
        return IEnhancedUserDataSchema
