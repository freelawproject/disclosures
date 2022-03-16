Courtlistener Disclosures
-------------------------

## Notes

This is a microservice of for extracting Financial Disclosure data used by Courtlistener.com.

The goal of this microservice is to isolate out these tools to let Courtlistener (a django site) be streamlined and easier to maintain. This service is setup to run with NGINX and gunicorn with a series of endpoints that accept financail disclosures and return JSON containing the content of a given financial disclosure.

In general, CL houses documents scraped and collected from hundreds of sources and these documents take many varied formats and versions.

## How to Use

This tool is designed to be connected securely from CL via a docker network called cl_net_overlay. But it can also be used directly by exposing port 5050. For more about development of the tool see the (soon coming) DEVELOPING.md file.

## Quick Start

Assuming you have docker installed run:

docker-compose -f docker-compose.yml up --build -d
This will expose the endpoints on port 5050, which can be modified in the nginx/nginx.conf file and points to the django server running on port 8000.

For more options and configuration of nginx checkout https://nginx.org/en/docs/.

After the compose file has finished you should be able to test that you have a working environment by running

    curl 0.0.0.0:5050
    curl http://localhost:5050

Should return and HTTP Response containing Heartbeat detected.

If connecting via the docker network you can test by running

    curl http://http://disclosures:5050

## Endpoints (Coming Soon)