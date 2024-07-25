from django.urls import path
from .views import ContactAPIView, EmailSubscriptionView, BookDemoView

urlpatterns = [
     path('contact/', ContactAPIView.as_view()),
     path('subscribe/', EmailSubscriptionView.as_view()),
     path('book_demo/', BookDemoView.as_view()),
]

