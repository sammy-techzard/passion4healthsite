from django.db import models
from wagtail.snippets.models import register_snippet

# Create your models here.
from django.db import models

from wagtail.models import Page
from wagtail.images.models import Image

from base.blocks import ServicesBlock, OverlappingImage, coreTeamBlock, CallForVolunteerBlock, DonationsFundScholarsBlock
from django.db import models
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

@register_snippet 
class OurService(models.Model):
    services = StreamField(
        ServicesBlock(),
    )
    def __str__(self):
        # Loop through the services stream field blocks
        for block in self.services:
            # Check if the block type is 'templated' (ServicesBlockStruct)
            if block.block_type == 'templated':
                # Return the 'snippet_title' from the block's value
                return block.value.get('snippet_title', 'No Title')

        # Fallback in case no title is found
        return "Unnamed Service"
    class Meta:
        verbose_name = "Our Service"
        verbose_name_plural = "Our Services"
        
        
@register_snippet
class WhyProjectSection(models.Model):
    block_title = models.CharField(
        verbose_name="Title of the Block",
        max_length=255
    )
    title = models.CharField(
        verbose_name="Main Title",
        max_length=255
    )
    
    content = models.TextField(
        verbose_name="Content Description",
    )
    
    images = StreamField(
        OverlappingImage(),
        
    )
    more_about_us = models.ForeignKey(
        'wagtailcore.Page',  # This allows selecting any page within the site
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Why project"
        verbose_name_plural = "Why projects"
    
@register_snippet
class OurTeam(models.Model):
    our_team = StreamField(
        coreTeamBlock(),
    )

    def __str__(self):
        # Loop through the blocks in the our_team StreamField
        for block in self.our_team:
            if block.block_type == 'templated':
                return block.value.get('block_title', 'No Title')

        # Fallback in case no block_title is found
        return "Unnamed Team"

    class Meta:
        verbose_name = "Our Team"
        verbose_name_plural = "Our Team"
        
        
@register_snippet
class BecomeVolunteerSection(models.Model):
    theblock = StreamField(
        CallForVolunteerBlock(),
        max_num =1,
        null = True,
        blank = True
    )
    def __str__(self):
        for block in self.theblock:
            if block.block_type == 'templated':
                return block.value.get('textshow', 'No Title')

        # Fallback in case no block_title is found
        return "Unnamed Block"
    
    
@register_snippet
class DonationsFundsAndScholars(models.Model):
    block=StreamField(
        DonationsFundScholarsBlock(),
        max_num = 1
    )
    def __str__(self):
        return "Donations, Funds And Scholars data"
    
    class Meta:
        verbose_name = "Donations Funds and Scholars"
        verbose_name_plural = "Donations Funds and Scholars"
        
