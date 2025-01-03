from django.urls import path
from chatbot.views import index

urlpatterns = [
    path('', index)
]