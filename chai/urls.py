from django.urls import path
from .views import all_chai,order,notes,chaiDetails


urlpatterns = [
    path('', all_chai,name="all_chai"),
    path('note/', notes,name="notes"),
    path('<int:chai_id>/', chaiDetails, name='chai_detail'),
]
