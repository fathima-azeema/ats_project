from django.urls import path
from .views import ApplicantListView, ApplicantCreateView, ApplicantUpdateView, ApplicantDeleteView

urlpatterns = [
    path('', ApplicantListView.as_view(), name='applicant-list'),
    path('add/', ApplicantCreateView.as_view(), name='applicant-add'),
    path('<int:pk>/edit/', ApplicantUpdateView.as_view(), name='applicant-edit'),
    path('<int:pk>/delete/', ApplicantDeleteView.as_view(), name='applicant-delete'),
]

