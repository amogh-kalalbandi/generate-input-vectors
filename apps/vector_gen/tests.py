import json
import requests
from django.test import TestCase

from apps.auth.test_utils import hit_auth_api

TEST_INPUT_SENTENCE = 'What is the score today?'


class VectorGenerationTestCase(TestCase):
    """Create tests to verify vector generation."""

    @staticmethod
    def get_access_token():
        """Get JWT access token."""
        username = 'amogh.kulkarni@gmail.com'
        password = '' # Change this value to add the password of the user created.

        payload = {
            'email': username,
            'password': password
        }

        return hit_auth_api(payload)

    @staticmethod
    def hit_vector_gen_api(input_sentence, access_token=None):
        """Hit the locahost API and return the response dictionary."""
        URL = 'http://localhost:8000/api/get_input_vector/'

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        payload = {
            'input_sentence': input_sentence
        }

        response = requests.get(
            URL,
            headers=headers,
            params=payload
        )

        return response

    def test_authentication_api(self):
        """Test whether a response is sent or not when auth token is not passed."""
        response = VectorGenerationTestCase.hit_vector_gen_api(TEST_INPUT_SENTENCE)
        self.assertEqual(401, response.status_code)

    def test_vector_gen_reponse_length(self):
        """Test vector list length."""
        auth_response = VectorGenerationTestCase.get_access_token()

        vector_response = VectorGenerationTestCase.hit_vector_gen_api(TEST_INPUT_SENTENCE, access_token=auth_response['access'])
        response_dict = json.loads(vector_response.text)

        self.assertEqual(500, len(response_dict['input_vector']))

    def test_vector_output_range(self):
        """Test whether the vector list returned is within the range of number of words present in input."""
        auth_response = VectorGenerationTestCase.get_access_token()

        vector_response = VectorGenerationTestCase.hit_vector_gen_api(TEST_INPUT_SENTENCE, access_token=auth_response['access'])
        response_dict = json.loads(vector_response.text)

        # calculate number words in sentence
        max_range = len(TEST_INPUT_SENTENCE.split(' '))

        # check the numbers in the vector list.
        range_check = any(num > 0 and num < max_range for num in response_dict['input_vector'])

        self.assertEqual(True, range_check)


