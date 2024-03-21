from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
#    path("<int:pk>/", views.ReceieptView.as_view(), name='input'),
#    path("<int:pk>/store/", views.StoreView.as_view(), name='store'),
]