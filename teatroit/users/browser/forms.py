from zope.formlib import form
from zope.interface import implements
from plone.app.users.browser.register import RegistrationForm
from quintagroup.formlib.captcha import CaptchaWidget
from .interfaces import (
    IBasicRegistrationForm,
    IUtenteRegistration,
    ITeatroRegistration,
    ICompagniaRegistration,
    ICaptchaSchema,
    )


class BasicRegistrationForm(RegistrationForm):
    """ Subclass the standard registration form
    """

    implements(IBasicRegistrationForm)

    def _addCaptcha(self, fields):
        fields += form.Fields(ICaptchaSchema)
        fields['captcha'].custom_widget = CaptchaWidget


class UtenteRegistrationForm(BasicRegistrationForm):
    @property
    def form_fields(self):
        # Get the fields so we can fiddle with them
        myfields = super(BasicRegistrationForm, self).form_fields

        # Add a captcha field to the schema
        myfields += form.Fields(IUtenteRegistration)

        self._addCaptcha(myfields)

        # Return the fiddled fields
        return myfields


class TeatroRegistrationForm(BasicRegistrationForm):
    @property
    def form_fields(self):
        # Get the fields so we can fiddle with them
        myfields = super(BasicRegistrationForm, self).form_fields

        # Add a captcha field to the schema
        myfields += form.Fields(ITeatroRegistration)

        self._addCaptcha(myfields)

        # Return the fiddled fields
        return myfields


class CompagniaRegistrationForm(BasicRegistrationForm):
    @property
    def form_fields(self):
        # Get the fields so we can fiddle with them
        myfields = super(BasicRegistrationForm, self).form_fields

        # Add a captcha field to the schema
        myfields += form.Fields(ICompagniaRegistration)

        self._addCaptcha(myfields)

        # Return the fiddled fields
        return myfields
