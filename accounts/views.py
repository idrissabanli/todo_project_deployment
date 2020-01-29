from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
def login(request):
    return render(request, 'sign_in.html')


class CustomLoginView(LoginView):
    template_name = 'sign_in.html'
    form_class = CustomLoginForm