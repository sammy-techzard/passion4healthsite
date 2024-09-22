from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import BlogAndNewsArticle

class BlogAndNewsArticleAdmin(ModelAdmin):
    model = BlogAndNewsArticle
    menu_label = 'News Updates'  # Name of the menu item
    menu_icon = 'doc-full'  # Icon for the menu (optional)
    add_to_settings_menu = False  # Do not add to settings menu
    exclude_from_explorer = False  # Include in explorer view
    list_display = ('title', 'first_published_at', 'live')  # Display fields in list
    search_fields = ('title',)

# Register the custom admin class
modeladmin_register(BlogAndNewsArticleAdmin)
