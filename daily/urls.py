from django.urls import path

from . import views

urlpatterns=[
    path("daily/",views.RunListView.as_view()),
    path("daily/today",views.RunDetailView.as_view()),
    path("daily/create/",views.RunCreateView.as_view()),

]