# users/serializers.py
from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from .models import Profile

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["email", "password", "password2"]

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password, **validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data["email"], password=data["password"])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid credentials.")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["username", "first_name", "last_name", "bio", "profile_picture"]



class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ["id", "email", "profile"]

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        
        # update User fields (if any)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # update nested Profile
        if profile_data:
            profile = instance.profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        
        return instance


