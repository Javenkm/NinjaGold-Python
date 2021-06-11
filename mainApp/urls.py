from django.urls import path

from . import views

urlpatterns = [
    path('', views.index), # render the HTML
    path('process_money', views.process_money), #this will determine the amount of gold to add or subtract
    path('destroy_session', views.destroy)
]

