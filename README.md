# Web Scraper Project

## Introduction
This app scrapes data from ITJobsWatch and writes to a file on the local host. The aim of this project is to deploy the app on a virtual machine and build a CI/CD pipeline.

## Run app on local machine
1. Clone code and open with PyCharm.
2. Install any package and dependencies, these can be found in the requirements.txt file.
3. Run main.py file and confirm the app runs on the local host.

## Running local tests
1. Set test_env to `live` in the config.ini file
2. Run the following command `pip3 install -U pluggy`
3. Run
```bash
python -m pytest tests/
```
4. The following output should be displayed
![local tests](images/local_tests.png)


## CI Pipeline
1. Navigate to Jenkins
2. Configure the job.
3. Add the following commands to the build step
```bash
sudo apt-get update
# Install python pip module
sudo apt-get install python3-pip -y
# Install pytest
pip3 install -U pytest
# Install BeautifulSoup4
sudo pip3 install BeautifulSoup4
```

Testing 1    
Testing 2    
Testing 3 - checking failures are not pushed to main


## Ansible Playbook Deployment
# Ansible Configure Testing
```yaml
---
- name: provision web scraper app
  hosts: host_app
  gather_facts: yes
  become: True
  become_user: root
  become_method: sudo
  vars:
    DB_HOST: db_private_ip

  tasks:
    - name: apt update and upgrade
      apt:
        upgrade: "yes"
        update_cache: "yes"
        cache_valid_time: 86400

    - name: install list of packages
      apt:
        pkg:
        - python3
        - python3-pip
        state: present

    - name: Copy app files
      copy:
        src: /home/ubuntu/DevOpsProject-ItJobsWatch-master
        dest: /home/ubuntu/
        force: no

    - name: Install Pytest and BeautifulSoup4 using pip3
      pip:
        name:
          - pytest
          - BeautifulSoup4

    - name: Run tests
     # become: yes
      shell: python3 -m pytest tests/
      args:
        chdir: /home/ubuntu/DevOpsProject-ItJobsWatch-master

```

### Ansible EC2 Creation
1.
2. Create the following directory called group_vars/all
3. Create an Ansible Vault in this location using the following command:
```yaml
ansible-vault create file.yml
```
4. Copy the following code into your EC2 Playbook
```yaml
---
- hosts: local
  connection: local
  gather_facts: true
  become: true
  vars:
    key_name: eng74-aminah-aws-key
    region: eu-west-1
    image: ami-0dc8d444ee2a42d8a
    id: "Aminah scraper ec2"
    sec_group: sg-0ffa8596995f6f497
    subnet_id: subnet-0999fd0326fda2d3c
    ansible_python_interceptor: /usrs/bin/python3

  tasks:
    - name: Installing dependencies
      apt:
        name:
          - python
          - python-pip
          - python3
          - python3-pip
        state: latest
    - name: Installing pip dependencies
      pip:
        name:
          - boto
          - boto3
          - nose
          - tornado
          - awscli
        state: present

    - name: get instance facts
      ec2_instance_facts:
        aws_access_key: "{{ aws_access_key }}"
        aws_secret_key: "{{ aws_secret_key }}"
        region: "{{ region }}"
      register: result

    - name: create ec2 instance
      ec2:
        aws_access_key: "{{ aws_access_key }}"
        aws_secret_key: "{{ aws_secret_key }}"
        assign_public_ip: true
        key_name: "{{ key_name }}"
        id: "{{ id }}"
        vpc_subnet_id: "{{ subnet_id }}"
        group_id: "{{ sec_group }}"
        image: "{{ image }}"
        instance_type: t2.micro
        region: "{{ region }}"
        wait: true
        count: 1
        instance_tags:
          Name: eng74-aminah-scraper-ec2

  tags: ['never','create_ec2']

```
### Tests
Testing CD Pipeline
