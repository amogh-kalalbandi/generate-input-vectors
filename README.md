## generate-input-vectors

### This project generates input vectors based on the input sentence passed to an API. It has a basic JWT authentication API which is mandatory to call before calling the input vector generation API.

    - This project uses python, django, REST Framework, numpy, docker to build the service.

### To setup the app in your local, please follow the wiki link.

    - https://github.com/amogh-kalalbandi/generate-input-vectors/wiki


### How to scale this project to handle higher number of requests:

    - The statement and the responses can be saved to a database model. This data will help us understand which statement are common and regularly asked by the customers. This inturn helps in deciding what statements can be cached so that the API has a faster response to such requests.

    - The project right now can be deployed using docker. But when the application needs to be scaled to satisfy huge number of requests, It can be deployed using kubernetes where the containers can be auto scaled when the demand is higher and scaled down when the volume of request decreases.


### Things considered:

    - Since this is an API service. A simple JWT authentication is implemented to authenticate the user request.

    - The API processes the input statement to see the number of words present in the sentence. Based on the number, the input vectors are generated. The range within which the vectors are generated is directly linked to the number of words present in the sentence.

    - The requirement was to generate an input vector based on an input statement provided. This feels like a NLP problem where we are trying to extract tokens from the statement and creating an input vector to be fed into the ML algorithm. Thus I implemented a simple way to generate an input vector based on the statement provided.

### Code Enhancements:

    - The code is strucutred to have authentication as an different app. If this service starts getting consumed by different users with different access levels, the Authentication and Authorization can be implemented in the auth app where it can independent and isolated from rest of the codebase.

    - The vector generator is implemented in a different app. This gives the flexibility to extend the features of the app to actually save the results of the vector generator to a database model for further analysis.

    - All the utility functions/methods related to every app can be kept within it for better readability of the code.
