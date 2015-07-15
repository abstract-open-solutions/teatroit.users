from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class TeatroitUsersLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import teatroit.users
        xmlconfig.file('configure.zcml', teatroit.users, context=configurationContext)

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'teatroit.users:default')

TEATROIT_USERS_FIXTURE = TeatroitUsersLayer()
TEATROIT_USERS_INTEGRATION_TESTING = IntegrationTesting(bases=(TEATROIT_USERS_FIXTURE,), name="TeatroitUsersLayer:Integration")
