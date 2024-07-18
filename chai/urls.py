from django.urls import path
from .views import all_chai,order


urlpatterns = [
    path('', all_chai,name="all_chai"),
    path('order/', order,name="all_chai"),
]
