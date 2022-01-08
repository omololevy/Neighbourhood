from django.db import models
from django.contrib.auth import get_user_model
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField  
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.username}'
        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    profile_picture = CloudinaryField('image',null=True)
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    neighbourHood = models.ForeignKey('NeighbourHood',on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
  

    def __str__(self):
        return f'{self.user} '
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()
    
    @classmethod
    def filter_profile_by_id(cls, id):
        profile = Profile.objects.filter(user__id = id).first()
        return profile

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

class NeighbourHood(models.Model):
    Neighbourhood_name = models.CharField(max_length=100)
    Neighbourhood_location= models.CharField(max_length=100)
    Neighbourhood_image = CloudinaryField('image',null=True)
    about_Neighbourhood = models.TextField(null=True)
    occupants_count = models.IntegerField()
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    health_info = models.IntegerField(null=True, blank=True)
    police_info = models.IntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ["-pk"]
    
    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()
        
    @classmethod
    def get_neighbourhood_by_id(cls,id):
        neighbourhood = NeighbourHood.objects.filter(pk=id)
        return neighbourhood
    
    @classmethod
    def search_neighbourhood_by_search_term(cls,search_term):
        return cls.objects.filter(name__icontains=search_term).all()
    
    
    def __str__(self):
        return self.Neighbourhood_name
    
class Business(models.Model):
    business_name = models.CharField(max_length=100)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE,null=True)
    business_email = models.EmailField()
    about_business = models.TextField(null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    
    class Meta:
        ordering = ["-pk"]
    
    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()
        
    @classmethod
    def get_business_by_id(cls,id):
        business = Business.objects.filter(pk=id)
        return business
    
    @classmethod
    def get_business_by_neighbourhood(cls,id):
        business = Business.objects.filter(neighbourhood=id).all()
        return business
    
    @classmethod
    def search_business_by_search_term(cls,search_term):
        return cls.objects.filter(business_name__icontains=search_term).all()
    
    def __str__(self):
        return self.business_name


class Post(models.Model):
    title = models.CharField(max_length=100,null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    Neighbourhood= models.ForeignKey(NeighbourHood,on_delete=models.CASCADE,null=True)
    
    class Meta:
        ordering = ["-pk"]
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
        
    @classmethod
    def get_post_by_id(cls,id):
        post =Post.objects.filter(pk=id)
        return post
        
    @classmethod
    def get_posts_by_neighbourhood(cls,id):
        posts = Post.objects.filter(hood=id).all()
        return posts
    
    def __str__(self):
        return self.title
