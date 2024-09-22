from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from calendar_api.views import EventViewSet, CustomAuthToken, LogoutView, RegisterView

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    
    # Include the router URLs
    path('api/', include(router.urls)),
    
    # Custom authentication endpoints
    path('api/login/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),
    path('api/register/', RegisterView.as_view(), name='register'),
]

# Add the router URLs to the urlpatterns
urlpatterns += router.urls