from django.contrib.auth import login,logout,get_user_model, authenticate 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer,UserLoginSerializer,UserSerializer
from rest_framework import  status, permissions
from rest_framework.permissions import IsAuthenticated, AllowAny  
 
UserModel = get_user_model()


class UserRegister(APIView):
    permission_classes = [AllowAny,]
    def post(self,request):
        serializer = UserRegisterSerializer(data = request.data)

        if serializer :
            user=serializer.save()
            return Response({'message':'user registerd succesfully'})
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class UserLogout(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permissions_classes = (IsAuthenticated)

    def post(self,request):
        logout(request)

        return Response ({'message':'logout succesful'}, status=status.HTTP_200_OK)



    
class UserView(APIView):
    authentication_classes = (SessionAuthentication,BasicAuthentication)
    permissions_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user 
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)




class UserLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
       
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
        
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return Response({'message': 'Login successful'})
            else:
                return Response({'message': 'Wrong password or email'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)
