#!/bin/bash

set -e

# Activate service account used for GCP and set project config
gcloud auth activate-service-account --key-file=gcp-creds.json
gcloud --quiet config set project search-retrieval-172116 
gcloud --quiet config set compute/zone asia-east1-c

# Build and push Docker image
docker build -t gcr.io/search-retrieval-172116/flaskapp:latest .
docker login -u _json_key -p "$(cat gcp-creds.json)" https://gcr.io
docker push gcr.io/search-retrieval-172116/flaskapp:latest

# Deploy to Google Compute Engine instance
gcloud compute firewall-rules update test_app --allow tcp:80,tcp:443,tcp:8080
gcloud compute instances create-with-container --tags=test_app --machine-type=f1-micro --container-privileged --zone asia-east1-c --container-image=gcr.io/search-retrieval-172116/flaskapp:latest