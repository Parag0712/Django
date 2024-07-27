
from django.contrib import admin
from django.urls import path,include
from .views import home,about,contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', home,name="home"),
    path('about/', about, name="about"),
    path('contact/', contact,name="contact"),
    path('chai/', include('chai.urls')),

    path("__reload__/", include("django_browser_reload.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)