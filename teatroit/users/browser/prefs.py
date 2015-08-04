import copy

from zope.component import getMultiAdapter
from plone.app.users.browser.personalpreferences import UserDataPanel
from plone.app.users.browser.personalpreferences import UserDataConfiglet
from Products.Five.browser import BrowserView

from .. import _


class CustomizedUserDataConfiglet(UserDataConfiglet):

    def __call__(self):
        # we must do this on __call__ to get current member
        # because on init security stuff is not available yet!
        # XXX: we shoul make this machinery configurable
        # per user type and roles
        omitted_fields = [
            'pdelete',
            'compagnia_tipo',
            'location',
            'comune',
            'cap',
            'telefono',
            'home_page',
            'redazione_argomento'
        ]
        membership = getMultiAdapter((self.context, self.request),
                                     name=u'plone_tools').membership()

        if self.userid:
            member = membership.getMemberById(self.userid)
        else:
            member = membership.getAuthenticatedMember()

        if member and 'Redattore' in member.getRoles():
            omitted_fields = [x for x in omitted_fields
                              if not x.startswith('redazione_')]
            for x in ('comune',
                      'cap',
                      'telefono',):
                omitted_fields.remove(x)
        if member and 'Compagnia' in member.getRoles():
            omitted_fields = [x for x in omitted_fields
                              if not x.startswith('compagnia_')]
        self.form_fields = self.form_fields.omit(*omitted_fields)
        return super(CustomizedUserDataConfiglet, self).__call__()


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

    def __call__(self):
        # we must do this on __call__ to get current member
        # because on init security stuff is not available yet!
        # XXX: we shoul make this machinery configurable
        # per user type and roles
        omitted_fields = [
            'pdelete',
            'compagnia_tipo',
            'location',
            'comune',
            'cap',
            'telefono',
            'home_page',
            'redazione_argomento'
        ]
        membership = getMultiAdapter((self.context, self.request),
                                     name=u'plone_tools').membership()

        if self.userid:
            member = membership.getMemberById(self.userid)
        else:
            member = membership.getAuthenticatedMember()

        if member and 'Redattore' in member.getRoles():
            omitted_fields = [x for x in omitted_fields
                              if not x.startswith('redazione_')]
        self.form_fields = self.form_fields.omit(*omitted_fields)
        return super(UtenteDataPanel, self).__call__()


class TeatroDataPanel(UserDataPanel):
    def __init__(self, context, request):
        super(TeatroDataPanel, self).__init__(context, request)

        self.form_fields = self.form_fields.omit(*('portrait',
                                                   'pdelete',
                                                   'description',
                                                   'compagnia_tipo',
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
