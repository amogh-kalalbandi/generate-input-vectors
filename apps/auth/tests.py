import json
import requests
from django.test import TestCase

from test_utils import hit_auth_api


class AuthenticationTestCase(TestCase):
    """Test case to check if JWT token is correctly generated or not."""

    def test_jwt_token_creation(self):
        """Call the API with username and password to check if token is received or not."""
        username = 'amogh.kulkarni@gmail.com'
        password = '5$6x3vtxjTGWwnb'

        payload = {
            'email': username,
            'password': password
        }

        response_dict = hit_auth_api(payload)
        self.assertEqual(True, 'access' in response_dict)

    def test_invalid_credentials(self):
        """Test whether the api response contains error message."""
        username = ''
        password = ''

        payload = {
            'email': username,
            'password': password
        }

        response_dict = hit_auth_api(payload)
        self.assertEqual(True, 'message' in response_dict)
