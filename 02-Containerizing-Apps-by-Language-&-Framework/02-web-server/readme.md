# Nginx Static Website with Docker

## 🎯 Objective

Serve a static HTML website using Nginx inside a Docker container.

## 📚 Docker Concept

This scenario demonstrates:

- FROM
- COPY
- EXPOSE
- Docker port publishing with -p
- Nginx as a base image

## 🏗️ Project Structure

my-website/
├── Dockerfile
├── index.html
├── assets/
│   └── style.css
├── README.md
├── commands.md
└── notes.md

## 🔧 Dockerfile

FROM nginx:1.25-alpine

COPY index.html /usr/share/nginx/html/index.html
COPY assets/ /usr/share/nginx/html/assets/

EXPOSE 80

## 🛠️ Implementation

Build the image:

docker build -t my-website .

Run the container:

docker run -d --name my-website-container -p 8080:80 my-website

Open:

http://localhost:8080

## 👀 Expected Output

The static website should be displayed by Nginx.

## 🧪 Build Failure Scenario

Modify the COPY source to reference a file that does not exist.

The Docker build should fail during the COPY instruction.

## 🧪 Container Failure Scenario

Use an incorrect port mapping or override the inherited Nginx CMD with an inappropriate command.

## ✅ Success Scenario

The website is successfully served through:

http://localhost:8080


## 💡 Key Learnings

- COPY happens during image build.
- Nginx serves files from its configured web root.
- EXPOSE does not publish a port.
- -p publishes a host port to a container port.
- The Nginx base image already provides its default startup command.

## 🔄 Real-World Use Cases

This pattern can be used to package static websites, frontend builds, documentation sites, and other static web content into lightweight Nginx containers.