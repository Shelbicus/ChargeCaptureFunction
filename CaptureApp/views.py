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
    
def thanks_view(request):
    context={}
    if request.method == "POST":
        resp_form = ChargeForm(request.POST)
        if resp_form.is_valid():
            print(resp_form)
            print(resp_form.cleaned_data)
            print(resp_form.cleaned_data["patient_email"])
            print(resp_form.calcPrice())
    print(request)
    print(context)
    return render(request,"thanks.html", context)
    

# Create your views here.
