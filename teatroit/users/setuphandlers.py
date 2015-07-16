from plone.app.controlpanel.security import ISecuritySchema
from Products.CMFCore.utils import getToolByName
from .config import GROUPS

class SetupVarious:

    def __call__(self, context):

        # Ordinarily, GenericSetup handlers check for the existence of XML files.
        # Here, we are not parsing an XML file, but we use this text file as a 
        # flag to check that we actually meant for this import step to be run.
        # The file is found in profiles/default.

        if context.readDataFile('teatroit.users_various.txt') is None:
            return

        # Add additional setup code here
        site = context.getSite()

        # do something...
        self.installProducts(site)
        self.setupSelfRegistration(site)
        self.setupSelfRegistration(site)

    def setupGroups(self, site):
        acl_users = getToolByName(site, 'acl_users')
        portal_groups = getToolByName(site, 'portal_groups')
        for group_id, group_title, roles in GROUPS:
            if not acl_users.searchGroups(id=group_id):
                portal_groups.addGroup(group_id,
                                       title=group_title,
                                       roles=roles,
                                      )

    def setupSelfRegistration(self, site):
         ISecuritySchema(site).enable_self_reg = True

    def installProducts(self, site):
         """ Install traditional products without profile """
         portal_quickinstaller = getToolByName(site,
                                               'portal_quickinstaller')
         if not portal_quickinstaller.isProductInstalled('quintagroup.captcha.core'):
             portal_quickinstaller.installProduct('quintagroup.captcha.core')

def setupVarious(context):
    """ setup various step. Handles for steps not handled by a gs profile """
    handler = SetupVarious()
    handler(context)

