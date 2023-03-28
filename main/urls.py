from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', BlogListView.as_view(), name="mainpage"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('<int:pk>', BlogDetailView.as_view(), name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]