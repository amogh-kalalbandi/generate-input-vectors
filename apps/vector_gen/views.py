import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class GenerateInputVector(APIView):
    """Generate Input vectors based on sentence sent."""
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        """Authenticate the request and return the input vector."""
        input_sentence = request.GET.get('input_sentence')
        input_token_list = input_sentence.split(' ')

        # Calculate the number of words in the sentence and return the float values in that given range
        vector_list = np.random.uniform(0, len(input_token_list), 500)

        return Response({
            'input_vector': vector_list
        })


