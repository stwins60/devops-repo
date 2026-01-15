#!/bin/bash
set -e

ENVIRONMENT=${1:-staging}
IMAGE_TAG=${2:-latest}

echo "Deploying to $ENVIRONMENT environment..."
echo "Using image tag: $IMAGE_TAG"

# Deploy based on environment
case $ENVIRONMENT in
    staging)
        echo "Deploying to staging..."
        kubectl set image deployment/myapp myapp=myapp:$IMAGE_TAG -n staging
        kubectl rollout status deployment/myapp -n staging
        ;;
    production)
        echo "Deploying to production..."
        kubectl set image deployment/myapp myapp=myapp:$IMAGE_TAG -n production
        kubectl rollout status deployment/myapp -n production
        ;;
    *)
        echo "Unknown environment: $ENVIRONMENT"
        exit 1
        ;;
esac

echo "Deployment completed successfully!"
