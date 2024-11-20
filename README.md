# deeplearningproject
```
Lung X-ray Classification 
Data link: https://drive.google.com/file/d/1pfIAlurfeqFTbirUZ5v_vapIoGPgRiXY/view?usp=sharing
```

# Workflows

- constants
- config_entity
- artifact_entity
- components
- pipeline
- main

# How to setup
```
bash (creating venv)
a) Using conda
conda create -n lung python 3.8 -y
b) Using pip
python -m venv my_venv

activating virtual environment
a) Using conda
conda activate lungs
b) Using pip
my_venv\Scripts\activate

pip install -r requirements.txt

setup aws cli
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

configure aws credentials
aws configure 
AWS_ACCESS_KEY_ID=***
AWS_SECRET_ACCESS_KEY= ***
AWS_REGION = us-east-1

BentoML demo repo: https://github.com/entbappy/bentoml-demo
```

 