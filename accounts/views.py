

# accounts/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from accounts.models import Account
from django.contrib.auth import login, authenticate, logout
from accounts.forms import (RegistrationForm, 
                            AccountAuthenticationForm,
                            AccountUpdateForm)

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, username=username, password=raw_password)
            if account:   # https://stackoverflow.com/a/67902300/5965865
                login(request, account)
            return redirect('accounts_home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    
    return render(request, 'accounts/register.html', context)

    
# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"

def accounts_home_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    
    return render(request, 'accounts/accounts_home.html', context)

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('accounts_home')
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user: 
                login(request, user)
                return redirect('accounts_home')

    else: 
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'accounts/login.html', context)



def logout_view(request):
    logout(request)
    return redirect('home')

def account_view(request):

    if not request.user.is_authenticated:
        return redirect('login')
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(
            initial = {
                'email': request.user.email,
                'username': request.user.username,
            }
        )
    context['account_form'] = form
    return render(request, 'accounts/account.html', context)


class HelloView(TemplateView):
    template_name = 'accounts/hello.html'

# class AccountsHomeView(TemplateView):

#     template_name = 'accounts/accounts_home.html' #app level folder

#     accounts = Account.objects.all()
#     def get_context_data(self, **kwargs):
        
#         context ={}
#         accounts = Account.objects.all()
#         context['accounts'] = accounts
#         # context['accounts'] = accounts
#         # context = {
#         #     'accounts': accounts,
#         # }
#         # context = super(SLMHomePageView, self).get_context_data(**kwargs)
#         return context
        # return render(request, "slm_app/slm_home.html", context)