from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated  # Add this import
from django.contrib.auth import logout
from .models import Event
from .serializers import EventSerializer, UserSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling CRUD operations on Event objects.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated for all actions

    def get_queryset(self):
        """
        Override to return only events belonging to the current user.
        """
        return Event.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Override to set the user of the event to the current user when creating.
        """
        serializer.save(user=self.request.user)

class CustomAuthToken(ObtainAuthToken):
    """
    Custom view for obtaining an auth token.
    Extends the built-in ObtainAuthToken view to return additional user info.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class LogoutView(APIView):
    """
    View for handling user logout.
    Deletes the user's auth token, effectively logging them out.
    """
    def post(self, request):
        # Delete the user's token
        request.auth.delete()
        # Log the user out
        logout(request)
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)

class RegisterView(APIView):
    """
    View for handling user registration.
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)