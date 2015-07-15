import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from teatroit.users.tests import \
    TEATROIT_USERS_INTEGRATION_TESTING


class TestRoles(unittest.TestCase):

    layer = TEATROIT_USERS_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']

    def test_roles(self):
        valid_roles = self.portal.valid_roles()
        from ..config import GROUPS
        teatroit_roles = []
        for item in GROUPS:
            teatroit_roles.extend(item[2])
        teatroit_roles = set(teatroit_roles)
        for role in teatroit_roles:
            assert role in valid_roles
