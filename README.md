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


