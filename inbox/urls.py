from django.urls import path
from . import  views

app_name='inbox'
urlpatterns = [
    path('send/message/', views.MessageSendView.as_view(), name='send_message'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.MessageDetailView.as_view(), name='detail'),
]