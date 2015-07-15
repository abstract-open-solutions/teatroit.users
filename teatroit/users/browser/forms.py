from zope.formlib import form
from zope.interface import implements
from plone.app.users.browser.register import RegistrationForm
from quintagroup.formlib.captcha import CaptchaWidget
from .interfaces import (
    IBasicRegistrationForm,
    ICaptchaSchema,
    )


class BasicRegistrationForm(RegistrationForm):
    """ Subclass the standard registration form
    """

    implements(IBasicRegistrationForm)

    @property
    def form_fields(self):
        # Get the fields so we can fiddle with them
        myfields = super(BasicRegistrationForm, self).form_fields

        # Add a captcha field to the schema
        myfields += form.Fields(ICaptchaSchema)
        myfields['captcha'].custom_widget = CaptchaWidget

        # Perform any field shuffling here...

        # Return the fiddled fields
        return myfields
