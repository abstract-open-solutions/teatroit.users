# -*- extra stuff goes here -*-
from zope.i18nmessageid import MessageFactory
from .config import PROJECTNAME

teatroitUsersMessageFactory = MessageFactory(PROJECTNAME)
_ = teatroitUsersMessageFactory


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
