from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Post,NeighbourHood,Business,Profile,User

class ProfileTestClass(TestCase):
    #setup method
    def setUp(self):
        self.user = Profile(user='Levy')
        self.user.save()
        self.user_profile = Profile(user=self.user, profile_picture="photore.png", bio="My bio")
   
    def tearDown(self):
       
        Profile.objects.all().delete()
      
    def test_instance(self):
        self.assertTrue(isinstance(self.user_profile,Profile))
            
    def test_save_user_profile(self):
        self.user_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
    def test_delete_user_profile(self):
        self.user_profile.save_profile()
        self.user_profile.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)==0)

class NeighbouhoodTestClass(TestCase):
    #setup method
    def setUp(self):
        self.user = Profile(name='Levy')
        self.user.save()
        self.user_profile = Profile(user=self.user,profile_picture="photore.png",bio="My bio")
        self.hood= NeighbourHood(hood_name="Dala",hood_location="Nairobi",occupants_count=10,admin=self.user_profile)
        
   
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        NeighbourHood.objects.all().delete()
      
    def test_instance(self):
        self.assertTrue(isinstance(self.hood,NeighbourHood))
            
    def test_save_neighbourhood(self):
        self.hood.save_neighbourhood()
        hoods=NeighbourHood.objects.all()
        self.assertTrue(len(hoods)>0)
        
    def test_delete_neighbourhood(self):
        self.hood.save_neighbourhood()
        self.hood.delete_neighbourhood()
        hood=NeighbourHood.objects.all()
        self.assertTrue(len(hood)==0)
        
        
class BusinessTestClass(TestCase):
    #setup method
    def setUp(self):
        self.user = User(username='Levy')
        self.user.save()
        self.user_profile = Profile(user=self.user,profile_picture="photore.png",bio="My bio")
        self.user_profile.save()
        self.hood= NeighbourHood(hood_name="Dala",hood_location="Nairobi",occupants_count=10,admin=self.user_profile)
        self.hood.save()
        self.business = Business(business_name = "Kinyos",business_email="kinyozi@gmail.com",neighbourhood=self.hood,owner=self.user_profile)
        
   
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        NeighbourHood.objects.all().delete()
        Business.objects.all().delete()
      
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))
            
    def test_save_business(self):
        self.business.save_business()
        businesses=Business.objects.all()
        self.assertTrue(len(businesses)>0)
        
    def test_delete_business(self):
        self.business.save_business()
        self.business.delete_business()
        businesses=Business.objects.all()
        self.assertTrue(len(businesses)==0)



class PostTestClass(TestCase):
    #setup method
    def setUp(self):
        self.user = User(username='Levy')
        self.user.save()
        self.user_profile = Profile(user=self.user,profile_picture="photore.png",bio="My bio")
        self.user_profile.save()
        self.hood= NeighbourHood(hood_name="Dala",hood_location="Nairobi",occupants_count=10,admin=self.user_profile)
        self.hood.save()
        self.post = Post(title = "Test",post="Test post",hood=self.hood,user=self.user_profile)
        
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
        NeighbourHood.objects.all().delete()
        Post.objects.all().delete()
      
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))
            
    def test_save_post(self):
        self.post.save_post()
        posts=Post.objects.all()
        self.assertTrue(len(posts)>0)
        
    def test_delete_post(self):
        self.post.save_post()
        self.post.delete_post()
        posts=Post.objects.all()
        self.assertTrue(len(posts)==0)

