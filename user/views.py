from django.shortcuts import render, redirect
from .forms import  RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .import forms
from django.contrib.auth import logout as auth_logout
from django.shortcuts import get_object_or_404 
from car.models import Car
from .models import Purchase
from django.views.generic import ListView
#from .views import buy_car


# Create your views here.
def singup(request):
   # if not request.user.is_authenticated:
        if request.method == 'POST':
            form =  RegistrationForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account Created Successfully')
                form.save()
                print(form.cleaned_data)
                return redirect('login')  # Redirect to login page after successful signup
        else:
            form =  RegistrationForm()
        return render(request, 'register.html',{'form':form,'type':'login'})
    # else:
    #     return redirect('reg') 


# def user_login(request):
#         if request.method=="POST":
#             form=AuthenticationForm(request,request.POST)
#             if form.is_valid():
#                 user_name=form.cleaned_data['username']
#                 user_pass=form.cleaned_data['password']
#                 user= authenticate(username=user_name,password=user_pass)
#                 if user is not None:
#                     messages.success(request,'LogIn Successfull')
#                     login(request,user)
#                     return redirect ('profile')
#                 else:
#                     messages.success(request,'LogIn Unsuccessfull')
#                     return redirect ('reg')


#         else:
#             form=AuthenticationForm()
#             return render(request,'login.html',{'form': form})


# 
class UserLogInView(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('profile')



    def form_valid(self, form):
        messages.success(self.request,'LogIn Done!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request,'Off! Try Again....Your Info Is Incorrect')
        return super().form_invalid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='Login'




        return context




# def profile(request):
#     return render(request,'profile.html')
    
def password(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,data=request.POST)
        if form .is_valid():
            form.save()
            messages.success(request,"Password Updated Successfully")
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    
    else:
        form=PasswordChangeForm(user=request.user)


    return render(request,'password.html',{'form':form})
       
def logout(request):
    auth_logout(request)  # Call Django's built-in logout function
    return redirect('user_login')  # Redirect to the login page or another appropriate page
    


def edit_profile(request):
    if request.method=='POST':
         profile_form=forms.UserChangeData(request.POST,instance=request.user)
         if profile_form.is_valid():
            profile_form.save()
            messages.success(request,'Account Updated Successfully')
            return redirect('profile')
    
    else:
       profile_form=forms.UserChangeData(instance=request.user)


    return render(request,'update.html',{'form':profile_form})

def buy_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.user.is_authenticated:
        Purchase.objects.create(user=request.user, car=car)
        car.quantity -= 1  # Reduce quantity
        car.save()
        return redirect('profile')  # Redirect to the profile page
    else:
        return redirect('login')

class ProfileView(ListView):
    model = Purchase
    template_name = 'profile.html'
    context_object_name = 'purchases'

    def get_queryset(self):
        return Purchase.objects.filter(user=self.request.user).select_related('car')
