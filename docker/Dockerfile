FROM python:3.9-slim

RUN apt-get update
RUN apt-get install -y python3-pip \
            poppler-utils wget unzip bc

RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran \
        libpcre3-dev g++ libz-dev  \
        build-essential make pkg-config \
        libjpeg-dev libpng-dev libtiff-dev \
        nginx

#Install QPDF
COPY docker/install-qpdf.sh /opt/
RUN ["chmod", "+x", "/opt/install-qpdf.sh"]
RUN /opt/install-qpdf.sh

RUN apt-get install python3-opencv -y
RUN apt-get update --option "Acquire::Retries=3" --quiet=2 && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get install \
        --option "Acquire::Retries=3" \
        --no-install-recommends \
        --assume-yes \
        --quiet=2 \
        `# Image & OCR tools` \
        imagemagick \
        `# Other dependencies` \
        libffi-dev libxml2-dev libxslt-dev python-dev \
        tesseract-ocr libtesseract-dev libleptonica-dev

RUN apt-get remove -y wget unzip bc

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY disclosures /opt/app/disclosures
COPY manage.py /opt/app/
WORKDIR /opt/app

COPY nginx/nginx.conf /etc/nginx/conf.d

COPY docker/docker-entrypoint.sh /opt/app/
RUN ["chmod", "+x", "/opt/app/docker-entrypoint.sh"]
ENTRYPOINT ["/opt/app/docker-entrypoint.sh"]
