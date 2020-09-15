from django.urls import path
from .views import indexListView, blogDetailView

urlpatterns = [
    path('', indexListView.as_view(), name='index'),
    path('details/<int:pk>', blogDetailView.as_view(), name='details')
]