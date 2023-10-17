## How to setup this project

### You need to have docker installed in your local machine to set up this project.

        - Mac [https://docs.docker.com/desktop/install/mac-install/]
        - Windows [https://docs.docker.com/desktop/install/windows-install/]
        - Linux [https://docs.docker.com/desktop/install/linux-install/]

### Steps to setup this project in local:

-- This document assumes that you have forked the project and cloned to your local computer.

-- Create a new .env file in server folder. Copy the contents of env.example file in server folder to .env file. fill postgres as value to POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD.

-- Create a 50 character random string with special characters and fill the DJANGO_SECRET_KEY value with it.

-- Run the following command to start the docker container. This will start the docker container, installs all the packages required for running the project.

    docker-compose up -d --build

-- Once you have verfied that the docker containers are up, Run the following commands inside the project folder:

    docker-compose exec web bash
    python manage.py migrate

-- The above 2 commands logs into web container and runs the necessary migrations to setup the project. Post the above command execution, Run the following command within web container:

    python manage.py createsuperuser

    Enter the username, email and password for the django admin.

-- Once the super user is created, Redirect to following URL in your browser:

 http://localhost:8000/admin/

-- Enter the username and password of the superuser you created in the previous step. Once logged in, click on the Users model on the home page and create a new user which will help in our further steps. (remember the password entered).

-- Once the above steps are completed, you can hit the vector generation API using Postman app or using the following commands. This commands should be run in the termial of the computer. The following command works in Linux or Mac OS. If you are using window, then Postman is the best app to test this APIs.

    curl -X POST http://localhost:8000/api/auth/login/ \
        -H "Content-Type: application/json" \
        -d '{"email": "<username created in django admin>", "password": "<password created in django admin>"}'

-- This command gives you a python dictionary with refresh and access token. Copy the access token, and run the following command to get the input vectors. Same as above. If you are using windows, then these commands won't work.

    curl http://localhost:8000/api/get_input_vector/?input_sentence=What%20is%20the%20score%20today \
        -H "Authorization: Bearer <Access token>"

-- If you want to run the tests written tests.py file in the respective apps, you can run the following commands:

    python manage.py test apps/auth
    python manage.py test apps/vector_gen
