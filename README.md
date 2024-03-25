# Iot data handling system


## 🛠 Skills

Python, Fast-API, HTML

## Features
- integration of Rabbitmq for iot data handing with mqtt plugin
- publish and sibscribe mqtt messaging service
- integration of mongodb for data storage
- sending tempreture data by mail service configuration

## Installation

### Install + configure the project

#### 1. Linux

```
# Create python virtual environment
python3 -m venv venv

# Activate the python virtual environment
source venv/bin/activate

# Install the requirements for the project into the virtual environment
pip install -r requirements.txt
```

#### 2. Windows

```
# Create python virtual environment
conda create --name venv python=3.10

# Activate the python virtual environment
conda activate venv

# Upgrade pip version
python -m pip install --upgrade pip

# Install the requirements for the project into the virtual environment in the following sequence:
pip install -r requirements.txt
```

## Install the dependencies of Fast API

pip install gunicorn
pip install "fastapi[all]"

## RabbitMQ Start and Stop 
net stop RabbitMQ && net start RabbitMQ

## Enable plugin configuration
rabbitmq-plugins enable rabbitmq_management