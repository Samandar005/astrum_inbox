from django.shortcuts import render
from django.views.generic import View, FormView
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import MessageForm


class HomePageView(View):
    def get(self, request):
        return render(request, 'index.html')

class MessageSendView(FormView):
    template_name = 'messages/send-message.html'
    form_class = MessageForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        super().form_valid(form)
        msg = f"Salom bu xabar {form.cleaned_data['from_email']} dan\n{form.cleaned_data['message']}"
        email = EmailMessage(
            form.cleaned_data['subject'],
            msg,
            settings.EMAIL_HOST_USER,
            [form.cleaned_data['to_email']]
        )
        email.send()
        return HttpResponseRedirect(self.success_url)
