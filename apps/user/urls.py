from django.urls import path
from .views import Create, Read, Update, Delete, List

urlpatterns = [
    path('create/', Create.as_view({'post': 'create'}), ),
    path('read_all/', List.as_view({'get': 'list'})),
    path('read/<id>/', Read.as_view({'get': 'retrieve'})),
    path('update/<id>/', Update.as_view({'put': 'update'})),
    path('delete/<id>/', Delete.as_view({'delete': 'destroy'})),
]

