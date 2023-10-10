from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self,validated_data):
            user = UserModel(validated_data['email'])
            user = UserModel(validated_data['username'], unique=True)
            user.set_password(validated_data['password'])
            user.save()
            return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')

        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError({'detail': 'Invalid credentials'})
    return {'user': user}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email' )

       