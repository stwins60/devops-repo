# Web Application Chart

Helm chart for deploying web applications to Kubernetes.

## Features

- Deployment with configurable replicas
- Service with LoadBalancer/ClusterIP
- ConfigMap for configuration
- Secrets management
- Ingress support
- HPA (Horizontal Pod Autoscaler)

## Installation

```bash
helm install myapp ./01-web-app-chart
```

## Configuration

See [values.yaml](values.yaml) for configuration options.
