"""
URL configuration for projectname project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from cse import views

from cse.views import StudentReg, Studentlist ,Studentdetail , StudentUpdate, StudentDelete 

app_name='cse'

urlpatterns = [
    path('home', views.home, name = "home"),
    path('product', views.product, name = "product"),
    path('service', views.service, name = "service"),
    path('contact', views.contact, name = "contact"),
    path('aboutus', views.about, name = "aboutus"),
    path('students', views.students, name = "students"),
    

   path('studentreg', StudentReg.as_view(), name = 'studentreg'),
   path('<pk>/studentdetail', Studentdetail.as_view(), name = 'studentdetail'),
   path('',Studentlist.as_view(), name = 'studentlist'),
   path('<pk>/studentupdate',StudentUpdate.as_view(),name = 'studentupdate'),
   path('<pk>/studentdelete', StudentDelete.as_view(), name = 'studentdelete'),


]