from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import ContactFormSubmission
from django.contrib import messages
from wagtail_modeladmin.helpers import ButtonHelper
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class ContactFormButtonHelper(ButtonHelper):
    # Override the edit_button to rename it to "Respond"
    def edit_button(self, pk, classnames_add=None, classnames_exclude=None):
        if classnames_add is None:
            classnames_add = []
        if classnames_exclude is None:
            classnames_exclude = []
        classnames = self.edit_button_classnames + classnames_add
        cn = self.finalise_classname(classnames, classnames_exclude)
        return {
            "url": self.url_helper.get_action_url("edit", pk),
            "label": _("Respond"),  # Change label from 'Edit' to 'Respond'
            "classname": cn,
            "title": _("Respond to this submission"),
        }
    def add_button(self, classnames_add=None, classnames_exclude=None):
        return None  # Returning None will hide the "Add" button
class ContactFormSubmissionAdmin(ModelAdmin):
    model = ContactFormSubmission
    menu_label = "Inbox"
    menu_icon = "mail"
    list_display = ('name', 'email', 'subject', 'created_at', 'responded')
    search_fields = ('name', 'email', 'subject')
    button_helper_class = ContactFormButtonHelper  # Use the custom ButtonHelper
# Register the ModelAdmin class with Wagtail
modeladmin_register(ContactFormSubmissionAdmin)