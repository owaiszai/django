from courses.views import homepage,coursePage 
from django.contrib import admin
from django.urls import path 
from courses.views import coursePage ,MyCoursesList,checkout

from django.conf.urls.static import static
from django.conf import settings
from courses.views import homepage

urlpatterns = [
    path ('', homepage.home , name = 'home'),
    path('course/<str:slug>', coursePage , name = 'coursepage'),
    path('check-out/<str:slug>', checkout , name = 'check-out'),
   
    path('my-courses', MyCoursesList.as_view() , name = 'my-courses'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)