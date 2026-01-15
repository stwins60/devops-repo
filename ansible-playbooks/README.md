# Ansible Playbooks

Automation playbooks for server provisioning, configuration management, and application deployment.

## 📋 Overview

This directory contains Ansible playbooks and roles for automating infrastructure provisioning, configuration management, and application deployments across multiple environments.

## 🏗️ Directory Structure

```
ansible-playbooks/
├── ansible.cfg                # Ansible configuration
├── site.yml                   # Main playbook
├── requirements.yml           # Ansible Galaxy requirements
├── inventory/                 # Inventory files
│   ├── production/
│   │   └── hosts
│   ├── staging/
│   │   └── hosts
│   └── development/
│       └── hosts
├── group_vars/               # Group variables
│   ├── all.yml
│   ├── webservers.yml
│   └── databases.yml
├── host_vars/                # Host-specific variables
├── roles/                    # Ansible roles
│   ├── common/
│   ├── webserver/
│   ├── database/
│   └── application/
├── playbooks/                # Specific playbooks
│   ├── provision.yml
│   ├── deploy.yml
│   └── maintenance.yml
└── README.md
```

## 🚀 Prerequisites

- Ansible 2.9 or higher
- Python 3.6+
- SSH access to target hosts
- Sudo privileges on target hosts

## 📦 Installation

### Install Ansible

**macOS:**
```bash
brew install ansible
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ansible
```

**RHEL/CentOS:**
```bash
sudo yum install ansible
```

**Using pip:**
```bash
pip install ansible
```

### Install Required Collections

```bash
ansible-galaxy install -r requirements.yml
```

## ⚙️ Configuration

### Ansible Configuration

The `ansible.cfg` file contains default settings:

```ini
[defaults]
inventory = ./inventory/production/hosts
remote_user = ansible
host_key_checking = False
retry_files_enabled = False
```

### Inventory Setup

Create inventory files for each environment:

**inventory/production/hosts:**
```ini
[webservers]
web1.example.com
web2.example.com

[databases]
db1.example.com

[all:vars]
ansible_user=ansible
ansible_python_interpreter=/usr/bin/python3
```

### Variables

**group_vars/all.yml:**
```yaml
---
ntp_server: pool.ntp.org
timezone: UTC
```

**group_vars/webservers.yml:**
```yaml
---
nginx_port: 80
app_user: www-data
```

## 🎯 Usage

### Running Playbooks

**Run the main playbook:**
```bash
ansible-playbook site.yml
```

**Run with specific inventory:**
```bash
ansible-playbook -i inventory/staging/hosts site.yml
```

**Run specific tags:**
```bash
ansible-playbook site.yml --tags "webserver,database"
```

**Dry run (check mode):**
```bash
ansible-playbook site.yml --check
```

**Run with extra variables:**
```bash
ansible-playbook site.yml -e "app_version=1.2.3"
```

**Limit to specific hosts:**
```bash
ansible-playbook site.yml --limit webservers
```

### Ad-hoc Commands

**Ping all hosts:**
```bash
ansible all -m ping
```

**Check disk space:**
```bash
ansible all -m shell -a "df -h"
```

**Restart a service:**
```bash
ansible webservers -m service -a "name=nginx state=restarted" --become
```

**Copy files:**
```bash
ansible all -m copy -a "src=/local/file dest=/remote/file"
```

## 📚 Available Playbooks

### 1. Site Playbook (site.yml)

Main playbook that includes all roles:
```bash
ansible-playbook site.yml
```

### 2. Provision Playbook

Provision new servers:
```bash
ansible-playbook playbooks/provision.yml
```

### 3. Deploy Playbook

Deploy applications:
```bash
ansible-playbook playbooks/deploy.yml -e "app_version=1.0.0"
```

### 4. Maintenance Playbook

Perform maintenance tasks:
```bash
ansible-playbook playbooks/maintenance.yml
```

## 🎭 Roles

### Common Role

Base configuration for all servers:
- System updates
- User management
- SSH hardening
- Firewall configuration
- Monitoring agents

### Webserver Role

Nginx/Apache configuration:
- Install web server
- Configure virtual hosts
- SSL certificates
- Load balancing

### Database Role

Database server setup:
- Install MySQL/PostgreSQL
- Configure replication
- Backup configuration
- Performance tuning

### Application Role

Application deployment:
- Deploy application code
- Configure environment
- Manage services
- Rolling updates

## 🔐 Security Best Practices

### 1. Ansible Vault

Encrypt sensitive data:

```bash
# Create encrypted file
ansible-vault create group_vars/production/vault.yml

# Edit encrypted file
ansible-vault edit group_vars/production/vault.yml

# Run playbook with vault
ansible-playbook site.yml --ask-vault-pass
```

**vault.yml example:**
```yaml
---
vault_db_password: "secret_password"
vault_api_key: "secret_api_key"
```

### 2. SSH Key Management

Use SSH keys instead of passwords:
```bash
ssh-keygen -t rsa -b 4096
ssh-copy-id ansible@server.example.com
```

### 3. Privilege Escalation

Use `become` for sudo operations:
```yaml
- name: Install package
  apt:
    name: nginx
    state: present
  become: yes
```

## 🧪 Testing

### Syntax Check

```bash
ansible-playbook site.yml --syntax-check
```

### Lint Playbooks

```bash
ansible-lint site.yml
```

### Test with Vagrant

```bash
vagrant up
ansible-playbook -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory site.yml
```

### Molecule Testing

```bash
cd roles/webserver
molecule test
```

## 📊 Monitoring and Logging

### Enable Logging

In `ansible.cfg`:
```ini
[defaults]
log_path = ./ansible.log
```

### Callback Plugins

Enable profile_tasks for timing:
```ini
[defaults]
callbacks_enabled = profile_tasks, timer
```

## 🔄 Best Practices

1. **Idempotency**: Ensure playbooks can run multiple times safely
2. **Variables**: Use group_vars and host_vars for organization
3. **Roles**: Break down complex playbooks into reusable roles
4. **Tags**: Use tags for selective execution
5. **Handlers**: Use handlers for service restarts
6. **Templates**: Use Jinja2 templates for configuration files
7. **Version Control**: Keep playbooks in Git
8. **Documentation**: Document variables and usage
9. **Testing**: Test in staging before production
10. **Vault**: Encrypt all sensitive data

## 📝 Example Playbook

```yaml
---
- name: Configure Web Servers
  hosts: webservers
  become: yes
  
  vars:
    nginx_port: 80
    app_name: myapp
  
  tasks:
    - name: Install Nginx
      apt:
        name: nginx
        state: present
        update_cache: yes
    
    - name: Copy configuration
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: Restart Nginx
    
    - name: Ensure Nginx is running
      service:
        name: nginx
        state: started
        enabled: yes
  
  handlers:
    - name: Restart Nginx
      service:
        name: nginx
        state: restarted
```

## 🔗 Resources

- [Ansible Documentation](https://docs.ansible.com/)
- [Ansible Galaxy](https://galaxy.ansible.com/)
- [Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)

## 📄 License

This configuration is for educational and demonstration purposes.
