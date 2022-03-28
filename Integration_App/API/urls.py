from django.urls import path
from Integration_App.API import views

urlpatterns=[
    path('get_api/',views.ListView.as_view()),
    path('mix_api/<int:pk>/',views.DetailView.as_view()),


]