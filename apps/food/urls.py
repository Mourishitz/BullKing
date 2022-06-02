from django.urls import path
from .views import Create, Read, Update, Delete, List

urlpatterns = [
    path('list/', List.as_view({'get': 'list'})),
    path('create/', Create.as_view({'post': 'create'})),
    path('read/<name>/', Read.as_view({'get': 'retrieve'})),
    path('update/<name>/', Update.as_view({'put': 'update'})),
    path('delete/<name>/', Delete.as_view({'delete': 'destroy'})),
]
