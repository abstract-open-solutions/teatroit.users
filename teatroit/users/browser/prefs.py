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
        # TODO: to be fixed, inside __init__ we are always anonymous!
        if 'compagnie' in member_groups:
            self.form_fields = self.form_fields.omit(*('location',))
        elif 'teatri' in member_groups:
            pass
        else:
            self.form_fields = self.form_fields.omit(*('location',))
