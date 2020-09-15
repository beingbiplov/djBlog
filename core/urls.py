from django.urls import path
from .views import indexListView, blogDetailView, blogDeleteView

urlpatterns = [
    path('', indexListView.as_view(), name='index'),
    path('details/<int:pk>', blogDetailView.as_view(), name='details'),
    path('delete/<int:pk>', blogDeleteView.as_view(), name='delete'),
]