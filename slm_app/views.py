
from django.shortcuts import render  # function-based view
from django.views.generic import TemplateView, DetailView
from accounts.models import Account

def slm_home_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    return render(request, 'slm_app/slm_home.html', context)


class SignUpView(TemplateView):
    pass
# class SLMHomePageView(TemplateView):
#     model = Account
#     template_name = 'slm_app/slm_home.html' #app level folder
#     accounts = Account.objects.all()
#     def get_context_data(self, **kwargs):
#         accounts = Account.objects.all()
        
#         context= {
#             'accounts': accounts,
#         }

#         return context
        # return render(request, "slm_app/slm_home.html", context)