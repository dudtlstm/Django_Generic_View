from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', BlogListView.as_view(), name="mainpage"),
    path('create/', BlogCreateView.as_view(), name="create"),
    path('<int:pk>', BlogDetailView.as_view(), name="detail"),
    path('update/<int:pk>', BlogUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name="delete"),
    path('new/', new, name="new"),
    path('edit/<int:pk>', edit, name="edit"),
]