Containers on AWS Elastic Beanstalk: Deploying a Custom Nginx Application with Docker 🐳
This project documents the process of using Docker to create a custom container image and deploying it quickly using AWS Elastic Beanstalk.

🚀 Project Overview
--
The core of this project involved:

Understanding and working with Containers and Docker.

Running a base Nginx container.

Creating a custom Docker image that serves a personalized welcome page.

Deploying the custom image to the cloud using AWS Elastic Beanstalk.

📦 Understanding Containers and Docker
--
Concept	Definition	Key Role in Project
Containers	
Tools for packaging applications in a way that is easy for developers to run and share work efficiently within a team.

The executable software running the Nginx server with the custom specifications.

Container Image	
--
A template or blueprint for creating containers. Containers spawned from the same image will behave identically.


The template used to create the Nginx container, serving the custom index.html file.

Docker	
--
A platform for creating and managing containers, simplifying the process of working with them.

Used to create the container images and manage the containers locally.


Docker Desktop	
--
Software for using and interacting with Docker, making the overall experience easier.

The client used to interact with the Docker daemon.

Docker Daemon	
--
The "engine" for Docker that receives commands (e.g., from Docker Desktop or the terminal) and actually creates, manages, and controls the containers.

Executes the commands sent by the user (the client).

🛠️ Key Steps and Commands
--
1. Running a Base Nginx Image

Nginx is a web server that helps with serving web content and is often referred to as a proxy server for distributing traffic.

The following command was used to start a new container running the base Nginx image:

Bash
docker run -d -p 80:80 nginx

docker run: The command to start a new container.


-d: Flag to run the container in the background (detached mode).


-p 80:80: Flag to match port 80 in the host computer to the container's port 80.

nginx: Specifies the image to use.

2. Creating a Custom Image
A Dockerfile was used as a set of instructions to tell Docker how to build the custom container image.

The custom image was built using the nginx image as its base and was modified to replace the default welcome page with a custom index.html file.

Dockerfile Contents:

Dockerfile
FROM nginx:latest
COPY index.html /usr/share/nginx/html/
EXPOSE 80
The command used to build the custom image:

Bash
docker build .

docker build: The command used to build a custom image with the Dockerfile.


. : Indicates that Docker can find the Dockerfile in the current directory.

Note on Running the Custom Image: An issue was encountered where a running container was already using port 80. This was resolved by stopping the previous container to allow the new one to start.

The custom image successfully served the personalized message: "Hello from Damien's custom Docker image!".

☁️ Deploying with AWS Elastic Beanstalk
--

Elastic Beanstalk is an AWS service that simplifies the process of deploying applications in the cloud by abstracting away much of the work involved in setting up the cloud infrastructure.

Deploying the custom Docker image using Elastic Beanstalk took only 10 minutes, including the launch time of the application.

The application was successfully deployed and accessible via the Elastic Beanstalk environment URL, displaying the custom welcome message
