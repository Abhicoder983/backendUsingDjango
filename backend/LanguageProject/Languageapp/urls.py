from Languageapp import views
from django.urls import path
urlpatterns = [
    path('login/',views.studentlist.as_view()),
    path('', views.landing),
    path('form/', views.contactform)
   
]
