## Notes

As this is a microservice of Courtlistener, tests are designed to be run from a Mock Courtlistener instance
to verify that the service works as expected and also works across a docker network.  

## Quick start

    docker-compose -f docker-compose.dev.yml up --build -d


## Testing

Testing is set up with the following default that our tests are run from
a container on the same network as the Doctor machine.  This is modeled after
how we plan to use the Doctor image for CL.

    docker-compose -f docker-compose.dev.yml up --build -d

Starts the Doctor Container and the Mock CL Container that we run our tests from.

    docker exec mock_cl_disclosures python3 -m unittest disclosures.tests

This is a duplicate of the disclosures container, which we use for simplicity, but it
makes the requests across the docker network.

## Building Images

Use Make to push images to docker hub:

    make x86_push --file docker/Makefile -e VERSION=$(git rev-parse --short HEAD)

Or to generate local images to push later:

    make image --file docker/Makefile -e VERSION=$(git rev-parse --short HEAD)

We only use x86 for the docker hub to avoid an incorrect architecture on the server.
