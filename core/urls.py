from django.urls import path
from .views import indexListView, blogDetailView, blogDeleteView, blogCreateView, blogUpdateView

urlpatterns = [
    path('', indexListView.as_view(), name='index'),
    path('details/<int:pk>', blogDetailView.as_view(), name='details'),
    path('delete/<int:pk>', blogDeleteView.as_view(), name='delete'),
    path('add-new-blog', blogCreateView.as_view(), name='add-new-blog'),
    path('update/<int:pk>', blogUpdateView.as_view(), name='update'),
]