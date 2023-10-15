from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """Serializer class to verify user credentials."""
    email = serializers.EmailField()
    password = serializers.CharField()
