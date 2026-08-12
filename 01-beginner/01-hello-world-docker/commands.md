# Commands

## Create Demo

mkdir hello-world-docker
cd hello-world-docker
touch Dockerfile

## Build Image

docker build -t hello-world .

## Check Images

docker image ls

## Run Container

docker run --name hello-world-container hello-world

## Check Containers

docker ps
docker ps -a

## View Logs

docker logs hello-world-container

## Cleanup

docker rm hello-world-container
docker rmi hello-world