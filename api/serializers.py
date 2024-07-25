from rest_framework import serializers
from .models import Contact, EmailSubscription, DemoBook

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class EmailSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubscription
        fields = ['email']

class BookDemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoBook
        fields = ['name', 'phone', 'email']
