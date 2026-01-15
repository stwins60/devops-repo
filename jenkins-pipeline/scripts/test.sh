#!/bin/bash
set -e

echo "Starting test process..."

# Run tests based on project type
if [ -f "package.json" ]; then
    echo "Running Node.js tests"
    npm test
elif [ -f "pom.xml" ]; then
    echo "Running Maven tests"
    mvn test
elif [ -f "go.mod" ]; then
    echo "Running Go tests"
    go test ./...
elif [ -f "requirements.txt" ]; then
    echo "Running Python tests"
    pytest
else
    echo "Unknown project type"
    exit 1
fi

echo "Tests completed successfully!"
