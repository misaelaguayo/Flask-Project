#!/bin/bash

set -e
cd ..
# Activate service account used for GCP and set project config
gcloud auth activate-service-account --key-file=gcp-creds.json
gcloud --quiet config set project search-retrieval-172116 
gcloud --quiet config set compute/zone asia-east1-c

# Build and push Docker image
docker build -t gcr.io/search-retrieval-172116/flaskapp:latest .
docker login -u _json_key -p "$(cat gcp-creds.json)" https://gcr.io
docker push gcr.io/search-retrieval-172116/flaskapp:latest

# Deploy to Google Compute Engine instance
gcloud compute instances update-container testapp --container-privileged --zone asia-east1-c --tags=flaskapp --machine-type=f1-micro --container-image=gcr.io/search-retrieval-172116/flaskapp:latest