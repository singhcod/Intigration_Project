from django.urls import path
from Integration_App import views

urlpattern = [
    path('all_detail',views.get_all_detail),

]