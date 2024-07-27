from django.urls import path
from .views import all_chai,notes,chaiDetails,chai_store


urlpatterns = [
    path('', all_chai,name="all_chai"),
    path('note/', notes,name="notes"),
    path('store/', chai_store,name="chaistores"),
    path('<int:chai_id>/', chaiDetails, name='chai_detail'),
]
