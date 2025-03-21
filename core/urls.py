from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('delete/<int:id>', views.DeleteModal.as_view(), name='delete_employee'),
    path('create/', views.CreateView.as_view(), name='create_employee'),
    path('update/<int:id>', views.UpdateView.as_view(), name='update_employee'),
]
