from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import LandingPageView,HomePageView,NeighbourHoodCreateView,ProfileView,NeigbourhoodDetail,UpdateNeigbourhood,add_business,add_post,update_post,update_business,join_neighbourhood,leave_neighbourhood,update_profile
from base.views import SignupView
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView
)


urlpatterns = [
    path('home/', HomePageView,name='home'),
    path('', LandingPageView.as_view(),name='landing'),

    path('join_neighbourhood/<int:id>', join_neighbourhood,name="join_neighbourhood"),
    path('leave_neighbourhood/<int:id>', leave_neighbourhood,name="leave_neighbourhood"),


    path('create_hood/', NeighbourHoodCreateView.as_view(),name="create_hood"),
    path('hood/<int:id>', NeigbourhoodDetail,name="hood"),
    path('update_hood/<int:id>', UpdateNeigbourhood,name="update_hood"),
    path('add_business/<int:id>', add_business,name="add_business"),
    path('update_business/<int:id>', update_business,name="update_business"),
    path('add_post/<int:id>', add_post,name="add_post"),
    path('update_post/<int:id>', update_post,name="update_post"),
    
    
    path('profile/', ProfileView,name="profile"),
    path('update_profile/', update_profile,name="update_profile"),
    path('signup/', SignupView,name='signup'),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page = '/'),name='logout'),

]
 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

