#!/bin/bash
set -e

echo "Starting build process..."

# Detect project type and build accordingly
if [ -f "package.json" ]; then
    echo "Node.js project detected"
    npm install
    npm run build
elif [ -f "pom.xml" ]; then
    echo "Maven project detected"
    mvn clean package
elif [ -f "go.mod" ]; then
    echo "Go project detected"
    go build -o app
elif [ -f "requirements.txt" ]; then
    echo "Python project detected"
    pip install -r requirements.txt
else
    echo "Unknown project type"
    exit 1
fi

echo "Build completed successfully!"
