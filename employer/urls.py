from django.urls import path

from .views import ListCreateEmployerAPIView, EmployerDetailUpdateDeleteAPIView

urlpatterns = [
    path('employers/', ListCreateEmployerAPIView.as_view(), name='list-create-employer'),
    path('employers/<int:pk>/' , EmployerDetailUpdateDeleteAPIView.as_view(), name='detail-update-delete-employer'),


]