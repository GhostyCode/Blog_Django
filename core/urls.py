from django.contrib import admin
from django.urls import path,include

from . views import HomeView
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',HomeView.as_view() ,name="home" ),

    path('blog/',include('blog.urls', namespace='blog'))
]
