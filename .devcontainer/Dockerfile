FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y curl unzip make && \
    pip install --upgrade pip

# Install AWS CDK CLI
RUN npm install -g aws-cdk

# Install Python dependencies
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

WORKDIR /workspaces/cloudquant
