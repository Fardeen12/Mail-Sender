from django.shortcuts import render
from SendEmail.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
# Create your views here.
def sent(request):
    sub = forms.Sent()
    if request.method == 'POST':
        sub = forms.Sent(request.POST)
        subject = "Testing"
        message = 'Ignore it Just Testing Email Sending Through Django'
        recepient = str(sub['Email'].value())
        print(recepient)
        send_mail(subject, message,EMAIL_HOST_USER, [recepient])
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'send.html', {'form':sub})
