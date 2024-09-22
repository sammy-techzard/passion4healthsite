from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Subscriber
from .serializers import SubscriberSerializer
from django.shortcuts import render
from django.utils import timezone
import calendar


@api_view(['POST'])
def subscribe(request):
    serializer = SubscriberSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        
        # Check if the email already exists
        if Subscriber.objects.filter(email=email).exists():
            return Response({"detail": "This email is already subscribed."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create the new subscriber if email doesn't exist
        Subscriber.objects.create(email=email)
        
        # Optionally send a confirmation email here

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def adminindex(request):
    subscribers = Subscriber.objects.all()

    return render(request, 'wagtailsubscribers/index.html', {
        'subscribers': subscribers
    })
