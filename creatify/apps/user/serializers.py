from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        min_length=1,
        max_length=128
    )

    class Meta:
        model = User
        fields = ('id', 'email', 'password')

    def validate_email(self, value):
        """验证邮箱格式和唯一性"""
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("请输入有效的邮箱地址")

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("该邮箱已被注册")
        return value.lower()  # 统一转为小写

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )


class CustomTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        return data
