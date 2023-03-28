# OpenAI Service Skeleton
Use this repo to create a service that talks to OpenAI.

## Running the project locally

### Prerequisites
* Docker installed on your machine

To run the project, follow these steps:

1. Open a terminal window.
2. Navigate to the root directory of this project.
3. Run the following command to build the Docker image:
```shell
docker build -t open-ai-service .
```

This command will build a Docker image with the name specified after `-t`

4. Once the image has been built, you can run the Docker container using the following command:
```shell
docker run -p 8080:8080 open-ai-service
```
You can now make requests to your local dockerfile using `localhost:8080`.

# Deploying to Cloud Run

To deploy a new version, do the following:

1. Authenticate to GCloud
2. Run `gcloud run deploy`
3. The source code location should line up with the root directory of this repository
4. Service name should be `open-ai-service`. You can change the name
5. Region should be `us-central1`
6. For now, we are allowing unauthenticated invocations

For more information on deploying to Google Cloud, read their docs [here](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service#deploy).