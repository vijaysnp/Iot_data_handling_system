# Iot data handling system


## 🛠 Skills

Python, Fast-API

## Features
- integration of Rabbitmq for iot data handing
- integration of mongodb for data storage
- sending iot data by mail service configation

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
