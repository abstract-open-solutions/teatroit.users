import copy
from zope.formlib import form
from zope.component import getMultiAdapter
from zope.interface import implements
from plone.app.users.browser.register import RegistrationForm

from Products.CMFCore.utils import getToolByName

from quintagroup.formlib.captcha import CaptchaWidget
from .interfaces import (
    IBasicRegistrationForm,
    IUtenteRegistration,
    ITeatroRegistration,
    ICompagniaRegistration,
    ICaptchaSchema,
    )
from .. import teatroitUsersMessageFactory as _


class BasicRegistrationForm(RegistrationForm):
    """ Subclass the standard registration form
    """

    implements(IBasicRegistrationForm)

    def _addCaptcha(self, fields):
        fields += form.Fields(ICaptchaSchema)
        fields['captcha'].custom_widget = CaptchaWidget
        return fields

    def handle_join_success(self, data):
        super(BasicRegistrationForm, self).handle_join_success(data)
        user_id = data['username']
        group_id = self.GROUP_ID
        if group_id is not None:
            membership = getMultiAdapter((self.context, self.request),
                                         name=u'plone_tools').membership()
            member = membership.getMemberById(user_id)
            portal_groups = getToolByName(self.context, 'portal_groups')
            portal_groups.addPrincipalToGroup(member.getUserName(), group_id)
        return


class UtenteRegistrationForm(BasicRegistrationForm):
    GROUP_ID = None

    @property
    def form_fields(self):
        # Get the fields so we can fiddle with them
        myfields = super(BasicRegistrationForm, self).form_fields

        # let's keep safe if form_fields is empty (no mail settings)
        if myfields:
            # Add a captcha field to the schema
            myfields += form.Fields(IUtenteRegistration)
    
            myfields = self._addCaptcha(myfields)
    
        # Return the fiddled fields
        return myfields


class TeatroRegistrationForm(BasicRegistrationForm):
    GROUP_ID = 'teatri'

    @property
    def form_fields(self):
        # Get the fields so we can fiddle with them
        myfields = super(BasicRegistrationForm, self).form_fields

        # let's keep safe if form_fields is empty (no mail settings)
        if myfields:
            # update fullname title and description
            fullname_field = copy.copy(myfields['fullname'].field)
            fullname_field.title = _(u'Teatro')
            fullname_field.description = u''
            myfields['fullname'].field = fullname_field

            # Add a captcha field to the schema
            myfields += form.Fields(ITeatroRegistration)
    
            myfields = self._addCaptcha(myfields)
    
        # Return the fiddled fields
        return myfields


class CompagniaRegistrationForm(BasicRegistrationForm):
    GROUP_ID = 'compagnie'

    @property
    def form_fields(self):
        # Get the fields so we can fiddle with them
        myfields = super(BasicRegistrationForm, self).form_fields

        # let's keep safe if form_fields is empty (no mail settings)
        if myfields:
            # update fullname title and description
            fullname_field = copy.copy(myfields['fullname'].field)
            fullname_field.title = _(u'Compagnia')
            fullname_field.description = u''
            myfields['fullname'].field = fullname_field

            # Add a captcha field to the schema
            myfields += form.Fields(ICompagniaRegistration)
    
            myfields = self._addCaptcha(myfields)
    
        # Return the fiddled fields
        return myfields
