from django.urls import path

from . import views

urlpatterns = [
    path('',views.entry,name='entry'),
    path('loadcomments/<id>/',views.loadcomments,name="loadcomments"),
    path('user/<name>/',views.user,name="user")
]