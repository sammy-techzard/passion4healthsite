import os
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def inline_svg(file_field):
    # Check if the file exists and is an SVG
    if file_field and file_field.url.endswith('.svg'):
        try:
            # Remove "media" from the URL to avoid duplication in the path
            relative_path = file_field.url.replace(settings.MEDIA_URL, '')
            # Construct the full file path by combining MEDIA_ROOT and the corrected relative path
            file_path = os.path.join(settings.MEDIA_ROOT, relative_path.lstrip('/'))  # Ensure no leading slashes
            if os.path.exists(file_path):  # Check if the file exists
                with open(file_path, 'r', encoding='utf-8') as svg_file:
                    return mark_safe(svg_file.read())  # Inline the SVG content
            else:
                return 'File not found'
        except Exception as e:
            return f'Error: {str(e)}'  # Return the error if something goes wrong
    return 'Not an SVG file'
