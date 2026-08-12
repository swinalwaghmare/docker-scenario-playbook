# Notes

## Concept

This demo teaches the basic Dockerfile instructions:
FROM, RUN, and CMD.

## Important Syntax

FROM ubuntu:22.04

RUN echo "Hello from build time"

CMD ["echo", "Hello from the container!"]

## Build Time

RUN executes during:

docker build

## Runtime

CMD executes when:

docker run

## Image

The result of docker build.

## Container

A runtime instance created from an image.

## Common Mistakes

- Thinking RUN executes when the container starts.
- Thinking CMD executes during docker build.
- Expecting a container running echo to remain running.

## Interview Points

RUN executes during image construction, while CMD defines the default command executed when a container starts.

## Real-World Usage

RUN is commonly used to install packages and prepare an image.

CMD is commonly used to define the default application process.