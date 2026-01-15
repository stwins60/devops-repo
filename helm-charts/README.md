# Helm Charts for Kubernetes

Kubernetes package manager charts for deploying applications to K8s clusters.

## 📋 Overview

This directory contains Helm charts for deploying a sample web application to Kubernetes. Helm is a package manager for Kubernetes that helps you define, install, and upgrade complex Kubernetes applications.

## 🏗️ Chart Structure

```
helm-charts/
├── Chart.yaml              # Chart metadata
├── values.yaml             # Default configuration values
├── .helmignore            # Files to ignore when packaging
├── templates/             # Kubernetes manifest templates
│   ├── deployment.yaml    # Deployment configuration
│   ├── service.yaml       # Service configuration
│   ├── ingress.yaml       # Ingress configuration
│   ├── configmap.yaml     # ConfigMap configuration
│   ├── secret.yaml        # Secret configuration
│   ├── hpa.yaml          # Horizontal Pod Autoscaler
│   ├── _helpers.tpl      # Template helpers
│   └── NOTES.txt         # Post-installation notes
└── README.md             # This file
```

## 🚀 Prerequisites

- Kubernetes cluster (v1.20+)
- Helm 3.x installed
- kubectl configured to access your cluster

## 📦 Installation

### Install Helm

**macOS:**
```bash
brew install helm
```

**Linux:**
```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

**Windows:**
```bash
choco install kubernetes-helm
```

### Deploy the Chart

1. **Install the chart:**
```bash
helm install my-app ./helm-charts
```

2. **Install with custom values:**
```bash
helm install my-app ./helm-charts -f custom-values.yaml
```

3. **Install in a specific namespace:**
```bash
helm install my-app ./helm-charts --namespace production --create-namespace
```

## ⚙️ Configuration

### Key Configuration Values

| Parameter | Description | Default |
|-----------|-------------|---------|
| `replicaCount` | Number of replicas | `3` |
| `image.repository` | Container image repository | `nginx` |
| `image.tag` | Container image tag | `latest` |
| `image.pullPolicy` | Image pull policy | `IfNotPresent` |
| `service.type` | Kubernetes service type | `ClusterIP` |
| `service.port` | Service port | `80` |
| `ingress.enabled` | Enable ingress | `false` |
| `ingress.host` | Ingress hostname | `example.com` |
| `resources.limits.cpu` | CPU limit | `100m` |
| `resources.limits.memory` | Memory limit | `128Mi` |
| `autoscaling.enabled` | Enable HPA | `false` |
| `autoscaling.minReplicas` | Minimum replicas | `1` |
| `autoscaling.maxReplicas` | Maximum replicas | `10` |

### Custom Values Example

Create a `custom-values.yaml` file:

```yaml
replicaCount: 5

image:
  repository: myapp
  tag: "1.0.0"
  pullPolicy: Always

service:
  type: LoadBalancer
  port: 8080

ingress:
  enabled: true
  host: myapp.example.com
  tls:
    enabled: true

resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 250m
    memory: 256Mi

autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 20
  targetCPUUtilizationPercentage: 80
```

## 🔧 Management Commands

### List Installed Charts
```bash
helm list
helm list --all-namespaces
```

### Upgrade Release
```bash
helm upgrade my-app ./helm-charts
helm upgrade my-app ./helm-charts -f custom-values.yaml
```

### Rollback Release
```bash
helm rollback my-app
helm rollback my-app 1  # Rollback to specific revision
```

### Uninstall Release
```bash
helm uninstall my-app
helm uninstall my-app --namespace production
```

### Get Release Information
```bash
helm status my-app
helm get values my-app
helm get manifest my-app
```

### Dry Run (Test Installation)
```bash
helm install my-app ./helm-charts --dry-run --debug
```

## 🧪 Testing

### Lint the Chart
```bash
helm lint ./helm-charts
```

### Template Rendering
```bash
helm template my-app ./helm-charts
helm template my-app ./helm-charts -f custom-values.yaml
```

### Test Release
```bash
helm test my-app
```

## 📦 Packaging

### Package the Chart
```bash
helm package ./helm-charts
```

### Create Chart Repository
```bash
helm repo index . --url https://charts.example.com
```

## 🔍 Debugging

### Check Pod Status
```bash
kubectl get pods -l app.kubernetes.io/name=my-app
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

### Check Service
```bash
kubectl get svc -l app.kubernetes.io/name=my-app
kubectl describe svc my-app
```

### Check Ingress
```bash
kubectl get ingress
kubectl describe ingress my-app
```

## 📚 Best Practices

1. **Version Control**: Always version your charts using semantic versioning
2. **Values Files**: Use separate values files for different environments
3. **Secrets**: Never commit sensitive data; use Kubernetes secrets or external secret managers
4. **Resource Limits**: Always define resource requests and limits
5. **Health Checks**: Configure liveness and readiness probes
6. **Labels**: Use consistent labeling for better organization
7. **Documentation**: Keep NOTES.txt updated with deployment information

## 🔗 Additional Resources

- [Helm Documentation](https://helm.sh/docs/)
- [Helm Best Practices](https://helm.sh/docs/chart_best_practices/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)

## 📄 License

This chart is for educational and demonstration purposes.
