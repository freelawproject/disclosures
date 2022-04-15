FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y python3-pip \
        poppler-utils && \
    apt-get install -y --no-install-recommends \
        libpcre3-dev  \
        build-essential \
        libjpeg-dev libpng-dev libtiff-dev && \
    apt-get install python3-opencv -y && \
    apt-get install -y --no-install-recommends apt-utils && \
    apt-get install \
        --option "Acquire::Retries=3" \
        --no-install-recommends \
        --assume-yes \
        --quiet=2 \
        `# Image & OCR tools` \
        imagemagick python3-opencv \
        `# Other dependencies` \
        libffi-dev libxml2-dev libxslt-dev python-dev \
        tesseract-ocr libtesseract-dev libleptonica-dev

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY disclosures /opt/app/disclosures
COPY manage.py /opt/app/
WORKDIR /opt/app

EXPOSE 5050
CMD gunicorn disclosures.wsgi:application \
      --workers ${DISCLOSURE_WORKERS:-4} \
      --max-requests 1000 \
      --max-requests-jitter 100 \
      --timeout 3600 \
      --bind 0.0.0.0:5050