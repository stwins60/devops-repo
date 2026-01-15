# Jenkins CI/CD Pipeline

Comprehensive Jenkins pipeline configurations for automated build, test, and deployment workflows.

## 📋 Overview

This directory contains Jenkins pipeline configurations demonstrating various CI/CD patterns including declarative and scripted pipelines, multi-branch pipelines, and shared libraries.

## 🏗️ Directory Structure

```
jenkins-pipeline/
├── Jenkinsfile                    # Main declarative pipeline
├── Jenkinsfile.declarative        # Declarative pipeline example
├── Jenkinsfile.scripted          # Scripted pipeline example
├── Jenkinsfile.multibranch       # Multi-branch pipeline
├── pipelines/                    # Additional pipeline examples
│   ├── docker-build.jenkinsfile
│   ├── kubernetes-deploy.jenkinsfile
│   └── terraform-deploy.jenkinsfile
├── scripts/                      # Helper scripts
│   ├── build.sh
│   ├── test.sh
│   └── deploy.sh
├── shared-libraries/             # Shared pipeline libraries
│   └── vars/
│       ├── buildApp.groovy
│       ├── deployApp.groovy
│       └── notifySlack.groovy
└── README.md
```

## 🚀 Prerequisites

- Jenkins 2.x or higher
- Required Jenkins plugins:
  - Pipeline
  - Git
  - Docker Pipeline
  - Kubernetes
  - Credentials Binding
  - Slack Notification (optional)

## 📦 Pipeline Types

### 1. Declarative Pipeline

The main `Jenkinsfile` uses declarative syntax, which is the recommended approach:

```groovy
pipeline {
    agent any
    stages {
        stage('Build') { ... }
        stage('Test') { ... }
        stage('Deploy') { ... }
    }
}
```

**Features:**
- Structured and easy to read
- Built-in error handling
- Post-build actions
- Parallel execution support

### 2. Scripted Pipeline

`Jenkinsfile.scripted` uses Groovy-based scripted syntax for more flexibility:

```groovy
node {
    stage('Build') { ... }
    stage('Test') { ... }
    stage('Deploy') { ... }
}
```

**Features:**
- More flexible and powerful
- Full Groovy programming capabilities
- Complex conditional logic

### 3. Multi-Branch Pipeline

`Jenkinsfile.multibranch` automatically creates pipelines for each branch:

**Features:**
- Automatic branch detection
- Branch-specific configurations
- Pull request builds

## ⚙️ Configuration

### Setting Up Jenkins

1. **Install Jenkins:**
```bash
# Using Docker
docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts

# Or install directly on your system
```

2. **Install Required Plugins:**
   - Navigate to: Manage Jenkins → Manage Plugins
   - Install: Pipeline, Git, Docker Pipeline, Kubernetes

3. **Configure Credentials:**
   - Navigate to: Manage Jenkins → Manage Credentials
   - Add credentials for:
     - Git repositories
     - Docker registries
     - Cloud providers (AWS, GCP, Azure)
     - Kubernetes clusters

### Creating a Pipeline Job

1. **New Item** → **Pipeline**
2. **Pipeline Definition:** Pipeline script from SCM
3. **SCM:** Git
4. **Repository URL:** Your repository URL
5. **Script Path:** `jenkins-pipeline/Jenkinsfile`

### Environment Variables

Configure these in Jenkins or in the pipeline:

```groovy
environment {
    DOCKER_REGISTRY = 'docker.io'
    DOCKER_IMAGE = 'myapp'
    KUBE_NAMESPACE = 'production'
    SLACK_CHANNEL = '#deployments'
}
```

## 🔧 Pipeline Stages

### Standard Pipeline Flow

1. **Checkout**
   - Clone repository
   - Checkout specific branch/commit

2. **Build**
   - Compile code
   - Build Docker images
   - Create artifacts

3. **Test**
   - Unit tests
   - Integration tests
   - Code quality checks
   - Security scans

4. **Deploy**
   - Deploy to staging
   - Run smoke tests
   - Deploy to production
   - Health checks

5. **Post Actions**
   - Send notifications
   - Archive artifacts
   - Clean workspace

## 📝 Example Pipelines

### Basic Build and Test

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'npm install'
                sh 'npm run build'
            }
        }
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
    }
}
```

### Docker Build and Push

```groovy
pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("myapp:${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Push to Registry') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-credentials') {
                        docker.image("myapp:${env.BUILD_NUMBER}").push()
                    }
                }
            }
        }
    }
}
```

### Kubernetes Deployment

```groovy
pipeline {
    agent any
    stages {
        stage('Deploy to Kubernetes') {
            steps {
                kubernetesDeploy(
                    configs: 'k8s/*.yaml',
                    kubeconfigId: 'kubeconfig'
                )
            }
        }
    }
}
```

## 🧪 Testing

### Running Pipeline Locally

Use Jenkins Pipeline Linter:

```bash
curl -X POST -F "jenkinsfile=<Jenkinsfile" http://jenkins-url/pipeline-model-converter/validate
```

### Replay Pipeline

In Jenkins UI:
1. Go to a completed build
2. Click "Replay"
3. Modify the pipeline script
4. Run without committing changes

## 🔐 Security Best Practices

1. **Use Credentials Plugin**
   - Never hardcode secrets
   - Use Jenkins credentials store

2. **Limit Agent Access**
   - Use specific agents for sensitive operations
   - Implement agent labels

3. **Code Scanning**
   - Integrate SAST tools
   - Scan dependencies for vulnerabilities

4. **Audit Logging**
   - Enable audit logs
   - Monitor pipeline executions

## 📊 Monitoring and Notifications

### Slack Integration

```groovy
post {
    success {
        slackSend(
            color: 'good',
            message: "Build Successful: ${env.JOB_NAME} ${env.BUILD_NUMBER}"
        )
    }
    failure {
        slackSend(
            color: 'danger',
            message: "Build Failed: ${env.JOB_NAME} ${env.BUILD_NUMBER}"
        )
    }
}
```

### Email Notifications

```groovy
post {
    always {
        emailext(
            subject: "Build ${currentBuild.result}: ${env.JOB_NAME}",
            body: "Build ${env.BUILD_NUMBER} completed with status: ${currentBuild.result}",
            to: 'team@example.com'
        )
    }
}
```

## 🔄 Advanced Features

### Parallel Execution

```groovy
stage('Parallel Tests') {
    parallel {
        stage('Unit Tests') {
            steps { sh 'npm run test:unit' }
        }
        stage('Integration Tests') {
            steps { sh 'npm run test:integration' }
        }
    }
}
```

### Conditional Stages

```groovy
stage('Deploy to Production') {
    when {
        branch 'main'
    }
    steps {
        sh './deploy-prod.sh'
    }
}
```

### Input Steps

```groovy
stage('Approval') {
    steps {
        input message: 'Deploy to production?', ok: 'Deploy'
    }
}
```

## 📚 Resources

- [Jenkins Documentation](https://www.jenkins.io/doc/)
- [Pipeline Syntax Reference](https://www.jenkins.io/doc/book/pipeline/syntax/)
- [Best Practices](https://www.jenkins.io/doc/book/pipeline/pipeline-best-practices/)

## 📄 License

This configuration is for educational and demonstration purposes.
