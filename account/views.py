from django.shortcuts import render , redirect , reverse
from django.views.generic import FormView , TemplateView , CreateView , View
from account.models import OTP, User
from mixins import LoginRequirdMixins
from .form import LoginForm , SignupForms , CheckOtpCodes
from django.urls import reverse_lazy
from django.contrib.auth import login , authenticate , logout
import ghasedakpack
from random import randint
import requests
from django.utils.crypto import get_random_string
from uuid import uuid4
SMS = ghasedakpack.Ghasedak("8534236d76060f342738a94b4ca72c")
class LoginUserView(LoginRequirdMixins,FormView):
    template_name = 'account/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home')
    def form_valid(self, form):
        cd = form.cleaned_data
        user = authenticate(self.request , username = cd['username'], password = cd['password'])
        if user is not None:
            login(self.request , user)
            return redirect('home_app:home')
        else:
            form.add_error('username', 'invalid')
        return render(self.request, self.template_name, {'form': form})
class RegisterationView(FormView):
    form_class = SignupForms
    template_name = 'account/register.html'    
    def form_valid(self, form):
        cd = form.cleaned_data
        randcode = randint(1000 , 9999)
        SMS.verification({'receptor': cd['phone'] , 'type': '1','template': 'randcode','param1': randcode})
        token = str(uuid4())
        OTP.objects.create(phone=cd['phone'] , code = randcode , token=token )
        print(randcode)
        return redirect(reverse('account:check_otp') + f'?token={token}')
class CheckOtpCode(FormView):
    template_name = 'account/check_otp.html'
    form_class = CheckOtpCodes
    success_url = reverse_lazy('home_app:home')
    def form_valid(self, form):
        token = self.request.GET.get('token')
        cd = form.cleaned_data
        if OTP.objects.filter(token=token, code = cd['code']).exists():
            otp = OTP.objects.get(token=token)
            user , is_created = User.objects.get_or_create(phone=otp.phone)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(self.request , user)
            otp.delete()
            return redirect('account:login')
        else:
            form.add_error('code' , "invalid data")
            return render(self.request, self.template_name, {'form': form})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home_app:home')
    else:
        return redirect('home_app:home')
# class RegisterationView(View):
#     template_name = 'account/register.html'    
#     def get (self, request):
#         form = SignupForms()
#         return render (request, self.template_name , {'form': form})
#     def post (self, request):
#         form = SignupForms(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             randcode = randint(1000 , 9999)
#             SMS.verification({'receptor': cd['phone'] , 'type': '1','template': 'randcode','param1': randcode})
#             OTP.objects.create(phone=cd['phone'],code = randcode )
#             print(randcode)
#             return redirect(reverse('account:check_otp') + f'?phone={cd["phone"]}')
#         else:
#             form.add_error(cd["phone"] , "The information is not correct")
#         return render(request , self.template_name , {'form':form})
        


# class CheckOtpCode(View):
#     template_name = 'account/check_otp.html'
#     # form_class = CheckOtpCodes
#     def get(self, request):
#         form = CheckOtpCodes()
#         return render(request, self.template_name , {'form':form})
#     def post(self, request):
#         phone = self.request.GET.get('phone')
#         form = CheckOtpCodes(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             if OTP.objects.filter( phone=phone, code = cd['code']).exists():
#                 user = User.objects.create_user(phone=phone)
#                 login(request , user)
#                 return redirect('account:login')
#             else:
#                 form.add_error('code' , "invalid data")
#                 return render(request, self.template_name, {'form': form})
#         else:
#             form.add_error('code' , "invalid data")
#             return render(request, self.template_name , {'form': form})

    # def get(self, request):
    #     form = CheckOtpCode()
    #     return render(request,'account/check_otp.html',{'form':form})

    # def post(self, request):
    #     phone = request.GET.get('phone')
    #     form = CheckOtpCode()
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         if OTP.objects.filter(code = cd['code'] , phone=phone).exists():
    #             user = User.objects.create_user(phone=phone)
    #             login(request,user)
    #             return redirect('home_app:home')
    #     else:
    #         form.add_error('code' , "invalid data")

    #     return render(request , 'account/check_otp.html', {'form':form , 'name':'amir'} )

