from django.urls import path
from .views import indexListView

urlpatterns = [
    path('', indexListView.as_view(), name='index'),
]