
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm, UserForm, ProfileForm, ImagepostForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
#from userprofile.models import Imagepost

class HomeView(TemplateView):
    template_name = 'common/home.html'


class LoginoptionView(TemplateView):
    success_url = reverse_lazy('home')
    template_name = 'common/login-option.html'
  


  

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'common/register.html'

from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from userprofile.models import Profile
from django.contrib import messages

from .forms import SignUpForm, UserForm, ProfileForm, ImagepostForm

from userprofile.models import Profile, Imagepost
from django.shortcuts import render,redirect
#from django.core.urlresolvers import reverse
#from django.urls import reverse

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'common/profile.html'


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'common/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data,instance=request.user.profile )#
        print(request.user)
        print(request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



class DashboardView(LoginRequiredMixin, TemplateView):
    image_form = ImagepostForm
    template_name = 'common/dashboard.html'
   # login_url = reverse_lazy('home')

    
    def post(self, request):

        post_data = request.POST or None #Changed
        file_data = request.FILES or None
              
        image_form = ImagepostForm (post_data, file_data, instance=request.user) #modified
        print(image_form)

        if image_form.is_valid():
            #image_form = image_form(**self.cleaned_data)
            #new_image = Imagepost.objects(image=image_form.cleaned_data['image'])
            #image_form = ImagepostForm.objects.create_image(username=request.POST['username'], email=request.POST['email'],password=request.POST['password1'])
            # image_form = image_form()
            # new_image.save()
            image_form.save()
            messages.error(request, 'Your image is uploaded successfully!')
            return HttpResponseRedirect(reverse_lazy('dashboard')) #Changed        

        context = self.get_context_data(image_form=image_form)
        print(context)

        return self.render_to_response(context)     

    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)





   
# def dashboard(request):
     
#     if request.method == "POST":
#         form=ImagepostForm(data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             obj=form.instance
#             return HttpResponseRedirect(reverse('home'),{"obj":obj})  
#     else:
#         form=ImagepostForm()    
#     #img=Imagepost.objects.all()
#     return HttpResponseRedirect(reverse('dashboard'),{"form":form})


