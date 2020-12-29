from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate
def register(request):
    form=UserForm()
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account has been created'+ user)
            
    context={'form':form}
    return render(request,'form/register.html',context) 

# Create your views here.
