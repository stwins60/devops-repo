# Web Server Setup

Ansible playbook for setting up NGINX web servers.

## Features

- Install NGINX
- Configure virtual hosts
- SSL certificates
- Firewall rules
- Service management

## Usage

```bash
ansible-playbook -i inventory/hosts site.yml
```

## Variables

See `group_vars/webservers.yml` for configuration.
