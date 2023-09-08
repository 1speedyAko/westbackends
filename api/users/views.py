from django.contrib.auth import login
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.decorators import login_required


# Django views for user registration (users/views.py)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    # Handle user registration and return a response (e.g., JSON)
    if request.method == 'POST':
        # Extract registration data from request data
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        # Validate the data (e.g., check if the username is unique)
        # Create a new user if data is valid
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)  # Log the user in after registration

        # Optionally, generate and return an access token
        # ...

        return JsonResponse({'message': 'Registration successful'})
    return JsonResponse({'message': 'Invalid request method'}, status=400)


# users/views.py
@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        # Authenticate the user and generate a new token
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@login_required
def protected_view(request):
    # This view is protected, and only authenticated users can access it.
    return JsonResponse({'message': 'Welcome to the protected view!'})






