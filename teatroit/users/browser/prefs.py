from zope.formlib import form
from zope.component import getMultiAdapter
from plone.app.users.browser.personalpreferences import UserDataPanel

from .interfaces import (
    IUtenteRegistration,
    ITeatroRegistration,
    ICompagniaRegistration,
    )


class CustomizedUserDataPanel(UserDataPanel):
    def __init__(self, context, request):
        super(CustomizedUserDataPanel, self).__init__(context, request)

        self.form_fields = self.form_fields.omit(*('portrait',
                                                   'pdelete',
                                                   'description',
                                                   'home_page'))
        membership = getMultiAdapter((self.context, self.request),
                                     name=u'plone_tools').membership()
        member = membership.getAuthenticatedMember()
        member_groups = [group.getId() for group in member.getGroups()]
        if 'compagnie' in member_groups:
            self.form_fields = self.form_fields.omit(*('location',))
            self.form_fields += form.Fields(ICompagniaRegistration)
        elif 'teatri' in member_groups:
            self.form_fields += form.Fields(ITeatroRegistration)
        else:
            self.form_fields = self.form_fields.omit(*('location',))
            self.form_fields += form.Fields(IUtenteRegistration)