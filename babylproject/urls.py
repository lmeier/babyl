"""babylproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from blogs import views
from accounts import views as accounts_views

urlpatterns = [
    
    #for all auth
    # url(r'^accounts/', include('allauth.urls')),
    # url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
    # home_files, name='home-files'),
    url(r'^accounts/', include('allauth.urls')),

    path('', views.index, name='index'),
    path('signup/', accounts_views.signup, name='signup'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    
    # path('overview/', views.user_home, name="overview"),
    path('home/', views.home, name='home'),
    path('settings/', views.settings, name='settings'),
    path('new-babyl/', views.new_babyl, name='new_babyl'),
    path('admin/', admin.site.urls),
    path('<blog_slug>/new-post', views.new_post,  name="new_post"),
    path('<blog_slug>/', views.view_blog, name='view_blog'),
    path('<blog_slug>/<post_slug>/', views.view_post, name='view_post'),


    # Note that you do not necessarily need the URLs provided by 
    # django.contrib.auth.urls. Instead of the URLs login, logout, and 
    # password_change (among others), you can use the URLs 
    # provided by allauth: account_login, account_logout, 
    # account_set_password…


    #path(‘profile/<username>/, views.profile, name=‘profile’),

    #path('admin/', admin.site.urls),
]

#    #path('account/', include('registration.backends.simple.urls')),
#     url(r'^accounts/register/',
#         RegistrationView.as_view(success_url='/home/'),
#         name='django_registration_register'),
#     url(r'^accounts/', include('django_registration.backends.one_step.urls')),
#     url(r'^accounts/', include('django.contrib.auth.urls')),