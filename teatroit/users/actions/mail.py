from Acquisition import aq_inner
from zope.component import adapts
from zope.component.interfaces import ComponentLookupError
from zope.interface import Interface, implements
from zope.formlib import form

from plone.app.contentrules.browser.formhelper import AddForm, EditForm
from plone.app.vocabularies.groups import GroupsSource
from plone.app.vocabularies.users import UsersSource
from plone.app.form.widgets.uberselectionwidget import UberMultiSelectionWidget
from plone.contentrules.rule.interfaces import IRuleElementData, IExecutable

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFPlone.utils import safe_unicode

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from plone.stringinterp.interfaces import IStringInterpolator
from collective.contentrules.mailtogroup.actions.mail import (
    IMailGroupAction as IOriginalMailGroupAction,
    MailGroupAction as OriginalMailGroupAction,
    MailActionExecutor as OriginalMailActionExecutor,
    )


class IMailGroupAction(IOriginalMailGroupAction):
    """ """


class MailGroupAction(OriginalMailGroupAction):
    """
    The implementation of the action defined before
    """
    implements(IMailGroupAction, IRuleElementData)

    element = 'plone.actions.MailGroup2'

    @property
    def summary(self):
        groups = ', '.join(self.groups)
        members = ', '.join(self.members)
        return _(u"Email report to the groups ${groups} and the members \
${members} (teatroit)", mapping=dict(groups=groups, members=members))


class MailActionExecutor(OriginalMailActionExecutor):
    """The executor for this action.
    """
    adapts(Interface, IMailGroupAction, Interface)

    def __call__(self):
        portal_membership = getToolByName(aq_inner(self.context), 'portal_membership')
        portal_groups = getToolByName(aq_inner(self.context), 'portal_groups')

        members = set(self.element.members)
        
        recipients = set()

 
        for groupId in self.element.groups:
            group = portal_groups.getGroupById(groupId)

            if group and group.getProperties().get('email'):
                recipients.update([group.getProperties().get('email')], )
            if group and group.getProperties().get('Email2'):
                # let's update the recipients with our custom Email2
                recipients.update([group.getProperties().get('Email2')], )

            # no need to send emails to group members in teatroit
            # groupMembers = group.getGroupMemberIds()
            # for memberId in groupMembers:
            #    members.update([memberId, ])

        for memberId in members:
            member = portal_membership.getMemberById(memberId)
            if member and member.getProperty('email'):
                recipients.update([member.getProperty('email'), ])

        mailhost = getToolByName(aq_inner(self.context), "MailHost")
        if not mailhost:
            raise ComponentLookupError, 'You must have a Mailhost utility to \
execute this action'

        source = from_address = self.element.source
        urltool = getToolByName(aq_inner(self.context), "portal_url")
        portal = urltool.getPortalObject()
        email_charset = portal.getProperty('email_charset')
        if not source:
            # no source provided, looking for the site wide from email
            # address
            from_address = portal.getProperty('email_from_address')
            if not from_address:
                raise ValueError, 'You must provide a source address for this \
action or enter an email in the portal properties'
            from_name = portal.getProperty('email_from_name')
            source = "%s <%s>" % (from_name, from_address)

        obj = self.event.object
        event_title = safe_unicode(obj.Title())
        event_url = obj.absolute_url()
        # Not all items have a text-field:
        try:
            event_text = safe_unicode(obj.getText())
        except:
            event_text = ''
        interpolator = IStringInterpolator(obj)
        message = "\n%s" % interpolator(self.element.message)
        subject = interpolator(self.element.subject)

        # Convert set of recipients to a list:
        list_of_recipients = list(recipients)
        if not list_of_recipients:
            return False
        # Prepare multi-part-message to send html with plain-text-fallback-message,
        # for non-html-capable-mail-clients.
        # Thanks to Peter Bengtsson for valuable information about this in this post:
        # http://www.peterbe.com/plog/zope-html-emails
        mime_msg = MIMEMultipart('related')
        mime_msg['Subject'] = subject
        mime_msg['From'] = source
        # mime_msg['To'] = ""
        mime_msg['Bcc'] = ', '.join(list_of_recipients)
        mime_msg.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body
        # in an 'alternative' part, so message agents can decide
        # which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        mime_msg.attach(msgAlternative)

        # Convert html-message to plain text.
        transforms = getToolByName(aq_inner(self.context), 'portal_transforms')
        stream = transforms.convertTo('text/plain', message, mimetype='text/html')
        body_plain = stream.getData().strip()

        # We attach the plain text first, the order is mandatory.
        msg_txt = MIMEText(body_plain, _subtype='plain', _charset=email_charset)
        msgAlternative.attach(msg_txt)

        # After that, attach html.
        msg_txt = MIMEText(message, _subtype='html', _charset=email_charset)
        msgAlternative.attach(msg_txt)

        # Finally send mail.
        # Plone-4
        try:
            mailhost.send(mime_msg)

        # Plone-3
        except:
            mailhost.secureSend(mime_msg.as_string())

        return True


class MailGroupAddForm(AddForm):
    """
    An add form for the mail action
    """
    form_fields = form.FormFields(IMailGroupAction)
    label = _(u"Add Mail Group Action")
    description = _(u"A mail action can mail different groups and members.")
    form_name = _(u"Configure element")
    form_fields['groups'].custom_widget = UberMultiSelectionWidget
    form_fields['members'].custom_widget = UberMultiSelectionWidget

    def create(self, data):
        a = MailGroupAction()
        form.applyChanges(a, self.form_fields, data)
        return a


class MailGroupEditForm(EditForm):
    """
    An edit form for the mail action
    """
    form_fields = form.FormFields(IMailGroupAction)
    label = _(u"Edit Mail group Action")
    description = _(u"A mail action can mail different recipient.")
    form_name = _(u"Configure element")
    form_fields['groups'].custom_widget = UberMultiSelectionWidget
    form_fields['members'].custom_widget = UberMultiSelectionWidget
