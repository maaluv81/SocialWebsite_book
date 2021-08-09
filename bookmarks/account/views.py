from django.shortcuts import render 

from django.conf import settings

from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required

from .admin import UserCreationForm,UserChangeForm

from django.contrib import messages

from .models import Profile

from .forms import ProfileEditForm

user = get_user_model()

# Create your views here.

@login_required
def dashboard(request):
  return render(request,'account/dashboard.html',{'section':'dashboard'})

def register(request):
  if request.method == 'POST':
    user_form = UserCreationForm(request.POST)
    # print("USERFORM==>",user_form )
    if user_form.is_valid():
    # Create a new user object but avoid saving it yet
      new_user = user_form.save(commit=False)
    # Set the chosen password
      new_user.set_password(user_form.cleaned_data['password1'])
    # Save the User object
      
      new_user.save()
      Profile.objects.create(user=new_user)
      return render(request,
      'account/register_done.html',
      {'new_user': new_user})
  else:
      user_form = UserCreationForm()
      return render(request,
    'account/register.html',
    {'user_form': user_form})

@login_required
def edit(request):
  if request.method == 'POST':
    user_form = UserChangeForm(instance=request.user,data=request.POST)
    profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
    print('PROFILE_FORM==>', profile_form )
    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        messages.success(request, 'Profile updated successfully')
    else:
      messages.error(request, 'Error updating your profile')
  user_form = UserChangeForm(instance=request.user)
  profile_form = ProfileEditForm(instance=request.user.profile)
  return render(request,
          'account/edit.html',
          {'user_form': user_form,
          'profile_form': profile_form})



def user_page(request):
    # print("user==>" , user )
    print("user==>",request.user)
    obj = user.objects.get(email=request.user)
    # print("OBJECT -->" ,obj)
    return render(request,'account/dashboard.html',{'obj':obj})

