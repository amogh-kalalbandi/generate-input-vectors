from django.urls import path

from apps.vector_gen.views import GenerateInputVector

# List of all authentication APIs.
urlpatterns = [
    path('get_input_vector/', GenerateInputVector.as_view(), name='token_obtain_pair')
]
