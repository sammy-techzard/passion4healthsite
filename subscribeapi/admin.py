from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import Subscriber  # Import your Subscriber model

# Define a ModelAdmin class for Subscriber
class SubscriberAdmin(ModelAdmin):
    model = Subscriber  # The model you want to register
    menu_label = 'Subscribers'  # The label in the admin menu
    menu_icon = 'group'  # Choose an icon for the menu item (check Wagtail icons for options)
    list_display = ('email', 'subscribed_at')  # Fields to display in the list view
    search_fields = ('email',)  # Enable search by email

# Register the ModelAdmin class with Wagtail
modeladmin_register(SubscriberAdmin)
