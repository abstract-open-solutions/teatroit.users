import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from teatroit.users.tests import \
    TEATROIT_USERS_INTEGRATION_TESTING


class TestInstall(unittest.TestCase):

    layer = TEATROIT_USERS_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.portal_groups = getToolByName(self.portal, 'portal_groups')

    def test_groups(self):
        from ..config import GROUPS
        teatroit_group_ids = set([item[0] for item in GROUPS])
        group_ids = set(self.portal_groups.getGroupIds())
        assert len(group_ids.intersection(teatroit_group_ids)) == len(GROUPS)
