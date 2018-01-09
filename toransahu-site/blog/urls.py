from django.urls import path, include
#from rest_framework.urlpatterns import format_suffix_patterns
from blog import views
import blog
from rest_framework import routers


# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
#router = routers.SimpleRouter()
router.register(r'blog', views.BlogViewSet)
router.register(r'users', blog.views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('',include(router.urls)),
]

"""
to append a set of format_suffix_patterns in addition to the existing URLs.
"""
#urlpatterns = format_suffix_patterns(urlpatterns)
