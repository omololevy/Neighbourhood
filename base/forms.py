from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import NeighbourHood,Business,Post,Profile

User = get_user_model()

class NeighbourHoodCreateForm(forms.ModelForm):
    hood_image = forms.FileField(),
    class Meta:
        model= NeighbourHood
        fields = (
            'hood_name',
            'hood_location',
            'hood_image',
            'about_hood',
            'occupants_count',
            'health_info',
            'police_info'
            
        )
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields = (
            'business_name',
            'business_email',
            'about_business' 
        )
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = (
            'title',
            'post',
        )

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    fullname=forms.CharField(max_length=254)
    
    class Meta:
        model = User
        fields = ("username",'fullname', 'email',)
        

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture')
