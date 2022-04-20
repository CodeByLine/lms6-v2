from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# from slm_app.forms import AddStudentForm, EditStudentForm
from accounts.models import CustomUser, SessionYearModel, Staff, Course, Subject, Student

def showDemoPage(request):
    return render(request, 'demo.html')

def showLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else: 
        user=authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("staff_home"))
                # return HttpResponse("staff login "+str(user.user_type))  # check as string
                
            else:
                return HttpResponseRedirect(reverse("student_home"))
                # return HttpResponse("student login "+str(user.user_type))  # check as string
                
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")
    

def admin_home(request):
    return render(request,"hod_templates/home_content.html")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+request.user.user_type)
    else:
        return HttpResponse("Please Login first")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

def signup_admin(request):
    return render(request, "signup_admin_page.html")


def signup_staff(request):
    return render(request, "signup_staff_page.html")


def signup_student(request):
    courses=Course.objects.all()
    session_years=SessionYearModel.objects.all()
    context={
        "courses" : courses,
        "session_years" : session_years,
    }
    return render(request, "signup_student_page.html", context)

def do_signup_admin(request):
    username=request.POST.get('username')
    email=request.POST.get('email')
    password=request.POST.get('password')

    try:
        user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=1)
        user.save()
        # return HttpResponse("Admin created")
        # return render(request, "do_admin_signup_page.html")
        messages.success(request, "Signup successfull. Please login.")
        return HttpResponseRedirect(reverse("show_login"))
    except:
        messages.error(request, "Failed to signup.")
        return HttpResponseRedirect(reverse("show_login"))


def do_signup_staff(request):
    username=request.POST.get('username')
    email=request.POST.get('email')
    password=request.POST.get('password')
    address=request.POST.get('address')

    try:
        user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=2)
        user.staff_address=address
        user.save()
        # return HttpResponse("Admin created")
        # return render(request, "do_admin_signup_page.html")
        messages.success(request, "Signup successfull. Please login.")
        return HttpResponseRedirect(reverse("show_login"))
    except:
        messages.error(request, "Failed to signup.")
        return HttpResponseRedirect(reverse("show_login"))


def do_signup_student(request):
    first_name=request.POST.get("first_name")
    last_name=request.POST.get("last_name")
    username=request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")
    address=request.POST.get("address")
    # date_joined=request.POST.get("date_joined" )
    session_year_id=request.POST.get("session_year")
    course_id=request.POST.get("course")
    gender=request.POST.get("gender")

    # if request.FILES.get('profile_pic', False):
    profile_pic=request.FILES['profile_pic']
    fs=FileSystemStorage()
    filename=fs.save(profile_pic.name, profile_pic)
    profile_pic_url=fs.url(filename)
    # else:
    #     profile_pic_url=None
    try:
        user=CustomUser.objects.create_user(
        username=username,
        password=password,
        email=email,
        last_name=last_name,
        first_name=first_name,
        user_type=3
        )
        user.student.address=address
        course_obj=Course.objects.get(id=course_id)
        user.student.course_id=course_obj
        session_year=SessionYearModel.objects.get(id=session_year_id)
        user.student.session_year_id=session_year
        # user.student.date_joined=date_joined
        user.student.gender=gender
        user.student.profile_pic=profile_pic_url
        user.save()

        messages.success(request,"Successfully Added Student")
        return HttpResponseRedirect(reverse("show_login"))
    except:
        messages.error(request,"Failed to Add Student")
        return HttpResponseRedirect(reverse("show_login"))
        


# # accounts/views.py
# from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views.generic import TemplateView
# from accounts.models import Account
# from django.contrib.auth import login, authenticate, logout
# from accounts.forms import (RegistrationForm, 
#                             AccountAuthenticationForm,
#                             AccountUpdateForm)

# from course_catalog.models import Course

# def registration_view(request):
#     context = {}
#     if request.POST:
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             account = authenticate(email=email, username=username, password=raw_password)
#             if account:   # https://stackoverflow.com/a/67902300/5965865
#                 login(request, account)
#             return redirect('accounts_home')
#         else:
#             context['registration_form'] = form
#     else:
#         form = RegistrationForm()
#         context['registration_form'] = form
    
#     return render(request, 'accounts/register.html', context)

    
# # class SignUpView(CreateView):
# #     form_class = CustomUserCreationForm
# #     success_url = reverse_lazy("login")
# #     template_name = "registration/signup.html"

# def accounts_home_view(request):
#     context = {}
#     accounts = Account.objects.all()
#     context['accounts'] = accounts
    
#     return render(request, 'accounts/accounts_home.html', context)

# def login_view(request):
#     context = {}
#     user = request.user
#     if user.is_authenticated:
#         return redirect('accounts_home')
    
#     if request.POST:
#         form = AccountAuthenticationForm(request.POST)
#         if form.is_valid():
#             email = request.POST['email']
#             password = request.POST['password']
#             user = authenticate(email=email, password=password)

#             if user: 
#                 login(request, user)
#                 return redirect('accounts_home')

#     else: 
#         form = AccountAuthenticationForm()

#     context['login_form'] = form
#     return render(request, 'accounts/login.html', context)



# def logout_view(request):
#     logout(request)
#     return redirect('home')

# def account_view(request):

#     if not request.user.is_authenticated:
#         return redirect('login')
#     context = {}

#     if request.POST:
#         form = AccountUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.initial = {
#                 "email": request.POST['email'],
#                 "username": request.POST['username'],
#             }
#             form.save()
#             context['success_message'] = "Updated"
#     else:
#         form = AccountUpdateForm(
#             initial = {
#                 'email': request.user.email,
#                 'username': request.user.username,
#             }
#         )
#     context['account_form'] = form
#     return render(request, 'accounts/account.html', context)


# class HelloView(TemplateView):
#     template_name = 'accounts/hello.html'

# # class AccountsHomeView(TemplateView):

# #     template_name = 'accounts/accounts_home.html' #app level folder

# #     accounts = Account.objects.all()
# #     def get_context_data(self, **kwargs):
        
# #         context ={}
# #         accounts = Account.objects.all()
# #         context['accounts'] = accounts
# #         # context['accounts'] = accounts
# #         # context = {
# #         #     'accounts': accounts,
# #         # }
# #         # context = super(SLMHomePageView, self).get_context_data(**kwargs)
# #         return context
#         # return render(request, "slm_app/slm_home.html", context)