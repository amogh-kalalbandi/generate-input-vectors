from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response

from apps.auth.serializer import LoginSerializer

class LoginAPI(APIView):
    """API class used for generating JWT refresh and access token."""

    def post(self, request):
        """Validate username and password of the user and return the refresh and access token."""
        try:
            bad_user = False
            message = 'Successful Login'
            data = request.data
            serializer = LoginSerializer(data=data)

            if serializer.is_valid():
                email = serializer.data['email']
                password = serializer.data['password']

                user = authenticate(username=email, password=password)

                if user is None:
                    bad_user = True
                    message = 'Invalid credentials'
                else:
                    refresh = RefreshToken.for_user(user)

            if bad_user:

                return Response({
                    'message': message,
                    'data': {}
                })

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        except Exception as e:

            message = 'An issue occurred, Try after sometime.'
            return Response({
                'message': message,
                'data': {}
            })
