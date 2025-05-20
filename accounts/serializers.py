from rest_framework import serializers
from django.contrib.auth import  get_user_model
from django.contrib.auth.password_validation import validate_password
User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')
        read_only_fields = ('id', 'email')

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'password2']
        read_only_fields = ['id']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords don\'t match')
        validate_password(data['password'])
        return data

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user