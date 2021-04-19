from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('<int:course_id>', views.delete_index),
    path('<int:course_id>/destroy', views.destroy)
]