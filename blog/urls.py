# import Django's function path and views from the blog application
from django.urls import path
from . import views 

urlpatterns = [
	path('', views.post_list, name='post_list'), # assign a view post_list to the root URL.
]