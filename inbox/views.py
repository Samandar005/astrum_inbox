from django.shortcuts import render
from django.views.generic import View, FormView, DetailView
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .forms import MessageForm
from .models import Message

class HomePageView( LoginRequiredMixin, View):
    def get(self, request):
        messages = Message.objects.filter(to_email=request.user.email) if request.user.is_authenticated else []
        return render(request, 'index.html', {'messages': messages})

class MessageSendView(FormView):
    template_name = 'messages/send-message.html'
    form_class = MessageForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = self.request.user
        sender_email = user.email if user.is_authenticated else form.cleaned_data['from_email']
        sender_name = getattr(user, "get_full_name", lambda: sender_email)()

        msg = f"Salom, bu xabar {sender_name} ({sender_email}) dan\n\n{form.cleaned_data['message']}"

        email = EmailMessage(
            subject=form.cleaned_data['subject'],
            body=msg,
            from_email=settings.EMAIL_HOST_USER,
            to=[form.cleaned_data['to_email']]
        )
        email.send()

        Message.objects.create(
            from_email=sender_email,
            to_email=form.cleaned_data['to_email'],
            subject=form.cleaned_data['subject'],
            message=form.cleaned_data['message'],
            user=user if user.is_authenticated else None
        )

        return HttpResponseRedirect(self.success_url)

class MessageDetailView(DetailView):
    model = Message
    template_name = 'messages/message-detail.html'
    context_object_name = 'message'

