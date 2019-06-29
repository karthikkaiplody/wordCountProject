"""wordCount URL Configuration

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

from django.urls import path
from . import views

urlpatterns = [
    #Goes to the views.py and displays what is return there
    path('', views.home),
    #Goes to the home.html and returns
    path('homepage/', views.homepage, name= 'home'),
    # Displays the information about the page
    path('about/', views.about, name= 'about'),
    #Goes to the count.html and returns
    path('count/', views.count, name='count'),
    # Since we are changed the name in home.html (action="{% url 'count' %}")whichever url we give still goes to the correct # #location: referencing the url that way.
    path('countWords/', views.count, name='count'),
    #Goes to the views.py and displays what is return there
    path('cube/', views.cube),

]
