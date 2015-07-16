import copy
from zope.formlib import form
from zope.component import getMultiAdapter
from plone.app.users.browser.personalpreferences import UserDataPanel
from Products.Five.browser import BrowserView

from .interfaces import (
    IUtenteRegistration,
    ITeatroRegistration,
    ICompagniaRegistration,
    )
from .. import teatroitUsersMessageFactory as _


class CustomizedUserDataPanel(BrowserView):
    """ We detect the type of user and redirect to the proper
        user preferences form
    """

    def __call__(self):
        membership = getMultiAdapter((self.context, self.request),
                                     name=u'plone_tools').membership()
        member = membership.getAuthenticatedMember()
        member_groups = member.getGroups()
        response = self.request.RESPONSE
        if 'compagnie' in member_groups:
            url = '@@compagnia-personal-information'
        elif 'teatri' in member_groups:
            url = '@@teatro-personal-information'
        else:
            url = '@@utente-personal-information'
        response.redirect(url)


class UtenteDataPanel(UserDataPanel):
    def __init__(self, context, request):
        super(UtenteDataPanel, self).__init__(context, request)

        self.form_fields = self.form_fields.omit(*('portrait',
                                                   'pdelete',
                                                   'description',
                                                   'tipo',
                                                   'location',
                                                   'comune',
                                                   'cap',
                                                   'telefono',
                                                   'home_page'))


class TeatroDataPanel(UserDataPanel):
    def __init__(self, context, request):
        super(TeatroDataPanel, self).__init__(context, request)

        self.form_fields = self.form_fields.omit(*('portrait',
                                                   'pdelete',
                                                   'description',
                                                   'tipo',
                                                   'home_page'))
        # update fullname title and description
        fullname_field = copy.copy(self.form_fields['fullname'].field)
        fullname_field.title = _(u'Teatro')
        fullname_field.description = u''
        self.form_fields['fullname'].field = fullname_field


class CompagniaDataPanel(UserDataPanel):
    def __init__(self, context, request):
        super(CompagniaDataPanel, self).__init__(context, request)

        self.form_fields = self.form_fields.omit(*('portrait',
                                                   'pdelete',
                                                   'description',
                                                   'location',
                                                   'comune',
                                                   'cap',
                                                   'telefono',
                                                   'provincia',
                                                   'home_page'))
        # update fullname title and description
        fullname_field = copy.copy(self.form_fields['fullname'].field)
        fullname_field.title = _(u'Compagnia')
        fullname_field.description = u''
        self.form_fields['fullname'].field = fullname_field
