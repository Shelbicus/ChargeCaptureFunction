from django.shortcuts import render
from django.http import HttpResponse
from .forms import ChargeForm
from django.views.generic.edit import FormView
from django import forms

class ChargeView(FormView):
    template_name = 'home.html'
    form_class = ChargeForm
    success_url ='/thanks/'

class ResponseForm(forms.Form):
    test = "asdasd"


def home_view(request):
    context={}
    context['form']= ChargeForm()
    print(context)
    return render(request,"home.html", context)

from django.core.mail import send_mail
from django.conf import settings

def thanks_view(request):
    context={}
    if request.method == "POST":
        resp_form = ChargeForm(request.POST)
        if resp_form.is_valid():
            print(resp_form)
            print(resp_form.cleaned_data)
            patient_email = (resp_form.cleaned_data["patient_email"])
            cost = (resp_form.calcPrice())
            send_mail(
                subject = 'Account Balance',
                message = 'Your account balance is' + ' '+ '$' + str(cost), 
                from_email = 'thetesttester3@gmail.com',
                recipient_list = [patient_email],
                fail_silently= False
            )
            #send_mail(subject, message, from_email, recipient_list)
    return render(request,"thanks.html", context)
    

# Create your views here.
