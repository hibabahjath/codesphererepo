from django.shortcuts import render,redirect

from store.forms import SignUp,SignIn

from django.urls import reverse_lazy

from django.contrib.auth import authenticate,login,logout

from django.views.generic import View,FormView,CreateView,TemplateView

from django.contrib import messages

# Create your views here.

# class SignUpView(View):

#     template_name="register.html"

#     form_class=SignUp

#     def get(self,request,*args,**kwargs):

#         form_instance=self.form_class()

#         return render(request,self.template_name,{"form":form_instance})
    
#     def post(self,request,*args,**kwargs):

#         form_instance=self.form_class(request.POST)

#         if form_instance.is_valid():

#             form_instance.save()

#             messages.success("Account Created Successfully")

#             return redirect('signin')
        
#         else:

#             messages.error("Failed to Create Account")

#             return render(request,self.template_name,{"form":form_instance})

class SignUpView(CreateView):

    template_name="register.html"

    form_class=SignUp

    success_url=reverse_lazy("signin")

class SignInView(FormView):

    template_name="login.html"

    form_class=SignIn

    def post(self,request,*args,**kwargs):

        form_instance=self.form_class(request.POST)

        if form_instance.is_valid():

            uname=form_instance.cleaned_data.get("username")

            pwd=form_instance.cleaned_data.get("password")

            user_obj=authenticate(username=uname,password=pwd)

            if user_obj:

                login(request,user_obj)

                return redirect("index")
        
        return render(request,self.template_name,{"form":form_instance})

class IndexView(TemplateView):

    template_name="index.html"

class LogoutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")

# function based View
# def logout_view(request,*args,**kwargs):

#     logout(request)

#     return redirect("signin")
