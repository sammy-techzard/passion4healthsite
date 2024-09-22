# serializers.py
from rest_framework import serializers
from .models import ContactFormSubmission

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormSubmission
        fields = ['name', 'email', 'subject', 'message']