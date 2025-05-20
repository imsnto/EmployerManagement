from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Employer
from accounts.serializers import UserProfileSerializer

class EmployerSerializer(serializers.ModelSerializer):
    #user_name = serializers.SerializerMethodField()
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = Employer
        fields = ['id', 'contact_person_name', 'company_name', 'email', 'phone_number', 'address', 'created_at','user']
        read_only_fields = ['created_at', 'id', 'user']

    # def get_user_name(self, obj):
    #     return obj.user.first_name + ' ' + obj.user.last_name

    # def validate(self, attrs):
    #     print("validate")
    #     if Employer.objects.filter(email=attrs['email']).exists():
    #         raise serializers.ValidationError('Email already registered')
    #     return attrs

    def validate_email(self, val):
        print("email", val)
        if Employer.objects.filter(email=val).exists():
            raise serializers.ValidationError('Email already registered')
        return val

    def create(self, validated_data):
        user = self.context['request'].user
        employer = Employer.objects.create(
            user = user,
            **validated_data
        )
        return employer



