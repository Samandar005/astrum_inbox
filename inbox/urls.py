from django.urls import path
from . import  views

app_name='inbox'
urlpatterns = [
    path('send/message/', views.MessageSendView.as_view(), name='send_message'),
    path('detail/<int:pk>/', views.MessageDetailView.as_view(), name='detail'),
]