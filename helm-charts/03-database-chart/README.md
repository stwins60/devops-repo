# Database Chart

Helm chart for database deployments with StatefulSet.

## Features

- StatefulSet for stable pod identity
- PersistentVolumeClaims
- Headless service
- ConfigMap for initialization scripts

## Supported Databases

- PostgreSQL
- MySQL
- MongoDB

## Installation

```bash
helm install database ./03-database-chart
```
