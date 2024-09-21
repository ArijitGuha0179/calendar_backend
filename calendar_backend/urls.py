from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from calendar_api.views import EventViewSet, CustomAuthToken, LogoutView

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),
    # Add a root URL pattern
    path('', RedirectView.as_view(url='/api/', permanent=False), name='api_root'),
]