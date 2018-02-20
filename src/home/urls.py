"""Home App Urls."""
from django.urls import path, include
from .views import Home
from django.conf import settings
from django.conf.urls.static import static


app_name = 'home'
urlpatterns = [
    # path('', views.home, name='home'),
    path('', Home.as_view(), name='home'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
