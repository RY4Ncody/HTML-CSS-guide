from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='task'),
    path('<no>/',views.task_page,name="list"),
]
