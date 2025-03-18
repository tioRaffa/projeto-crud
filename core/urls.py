from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('delete/<int:id>', views.DeleteModal.as_view(), name='delete')
]
