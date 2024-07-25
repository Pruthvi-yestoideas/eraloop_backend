from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer, EmailSubscriptionSerializer,BookDemoSerializer

class ContactAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"results":serializer.data, "detail":"Thank you for contacting us! We will get back to you shortly."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmailSubscriptionView(APIView):
    def post(self, request):
        serializer = EmailSubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'results': 'You have successfully subscribed!'}, status=status.HTTP_201_CREATED)
        return Response({"detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class BookDemoView(APIView):
    def post(self, request):
        serializer = BookDemoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'results': 'Congratulations! Your booking has been successfully confirmed!'}, status=status.HTTP_201_CREATED)
        return Response({"detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
