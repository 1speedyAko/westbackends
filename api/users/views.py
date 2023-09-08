from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

class UserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        # Handle user registration and return a response (e.g., JSON)
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # Validate the data (e.g., check if the username is unique)
        if User.objects.filter(username=username).exists():
            return Response({'detail': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user if data is valid
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)  # Log the user in after registration

        # Optionally, generate and return an access token
        # ...

        return Response({'message': 'Registration successful'})

    def user_login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Authenticate the user and generate a new token
            token, created = Token.objects.get_or_create(user=user)

            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
