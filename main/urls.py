from django.urls import path
from . import views


# This is the url which is shows the viwes defined in the viwes.py file

urlpatterns = [
    path('', views.TutorialListView.as_view(), name='home'),
]