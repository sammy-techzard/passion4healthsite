# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactFormSerializer

@api_view(['POST'])
def contact_form_submission(request):
    serializer = ContactFormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # Optionally send a confirmation email here
        return Response({'message': 'Thank you for contacting us!'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
