# FastAPI Dockerized Application

## Prerequisites

To run this application, you need to have Docker installed on your machine. Please follow the official Docker installation guide based on your operating system: [Docker Installation](https://docs.docker.com/get-docker/).

## Getting Started

To get started with the FastAPI application, follow the steps below:

1. Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/hamidullaorifov/Bewise-Task-2.git
   ```
2. Go to work directory

    ```bash
   cd Bewise-Task-2
   ```
3. Build and start docker container
    ```bash
   docker-compose up --build
   ```

4. Access the FastAPI application
    Open your web browser and navigate to http://localhost:8000/docs. 

5. Stop the Docker container:
    ```bash
    docker ps  # Get the CONTAINER ID
    docker stop <CONTAINER_ID>
    
    
 ## Examples
 1. Create new user
 ![image](https://github.com/hamidullaorifov/Bewise-Task-2/assets/101413208/8901a8fa-4dc5-4b28-b0f6-a9b4c485ce5f)
 
 Response
 ![image](https://github.com/hamidullaorifov/Bewise-Task-2/assets/101413208/4cce3ff5-2559-4349-8711-f35e687265d9)
 
 2. Try to create user with username that already exist
 ![image](https://github.com/hamidullaorifov/Bewise-Task-2/assets/101413208/956025b7-0c45-41a1-96df-2eb81795de0b)
 
 Response
 ![image](https://github.com/hamidullaorifov/Bewise-Task-2/assets/101413208/2b8cb17a-d99a-4dd9-9178-23c6542ea362)
 
 3. Adding an audio recording with valid data
 ![image](https://github.com/hamidullaorifov/Bewise-Task-2/assets/101413208/801cbe63-453c-4d0d-b5a2-7220829fbc0f)

Response
![image](https://github.com/hamidullaorifov/Bewise-Task-2/assets/101413208/038ce366-5a5a-475a-ac2e-11de4606919e)

4. Try to add an audio recording with invalid user data
![image](https://github.com/hamidullaorifov/Bewise-Task-2/assets/101413208/f1f56315-7825-447b-8a68-522da5b98946)

Response
![image](https://github.com/hamidullaorifov/Bewise-Task-2/assets/101413208/ebeada8b-ce1d-47ea-8fbf-5ec499b2b7e9)

5. Try to add an audio recording with invalid file format
![image](https://github.com/hamidullaorifov/Bewise-Task-2/assets/101413208/bab8b4a9-4ed8-4152-9f71-a4beaad89712)


Response
![image](https://github.com/hamidullaorifov/Bewise-Task-2/assets/101413208/cd4d2647-c563-4c5b-83a1-3fe83cc735c9)

6. Paste response url to your browser
![image](https://github.com/hamidullaorifov/Bewise-Task-2/assets/101413208/3710095f-b6e9-4502-b83e-b98de0ca8628)

Result
![image](https://github.com/hamidullaorifov/Bewise-Task-2/assets/101413208/38e7917f-0126-4b05-babf-d25da1c9269e)





