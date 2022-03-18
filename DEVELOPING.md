## Notes

As this is a microservice of Courtlistener, tests are designed to be run from a Mock Courtlistener instance
to verify that the service works as expected and also works across a docker network.  

## Quick start

    docker-compose -f docker-compose.dev.yml up --build -d


## Testing

Testing is setup with the following default that our tests are run from
a container on the same network as the Doctor machine.  This is modeled after
how we plan to use the Doctor image for CL.

    docker-compose -f docker-compose.dev.yml up --build -d

Starts the Doctor Container and the Mock CL Container that we run our tests from.

    ddocker exec mock_cl_disclosures python3 -m unittest disclosures.tests

This is a duplicate of the disclosures container, which we use for simplicity, but it
makes the requests across the docker network.

## Building Images

A soon to be written make file will certainly be used to build and push images to docker hub.

    make x86_push --file docker/Makefile

you can use

    make image --file docker/Makefile

to generate the image in your own architecture (**cough cough Apple Silicon)

We only use x86 for the docker hub to avoid an incorrect architecture on the server.