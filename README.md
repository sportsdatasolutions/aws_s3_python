## AWS S3 and Python

> Steps to get [AWS S3 (Simple File Storage)](https://aws.amazon.com/s3/) ***setup*** and ***linked*** too your Python projects!

### Getting Started

> For **learning purposes**, ***recreate*** this repository on Github for yourself!

#### 1. To **start**, set up a project ***Locally*** or on ***Deepnote***. Take the time to have a look at our ***[Project Setup Templates for Python (Tutorial)](https://github.com/sportsdatasolutions/python_project_template)***. If you already have Local or Deepnote ***templates*** set up on Github, be sure to use them! Otherwise, do something like...

```markdown
## Local

#### 1. Make Github Repo (Readme, .gitignore)
#### 2. Clone Locally

$ git clone git@github.com:username/aws_s3_python.git && cd aws_s3_python
```

```markdown
## Deepnote

#### 1. Make Github Repo (Readme, .gitignore)
#### 2. Make Deepnote Project
#### 3. Link Github Repo to Deepnote Project
#### 4. Drag all files/folders into root of Deepnote Project, including .git, and delete empty folder
```

#### 2. Continue to follow steps below to set up your projects package (dependency) management. We'll specifically be using ```pipenv```. Note [this guide](https://realpython.com/pipenv-guide/) if it's your first time using ```pipenv```.

#### ```Dependencies```

> If you have your own environment **with ```pipenv``` setup**, simply see [Pipfile](./Pipfile) and install required packages. Otherwise, install ```pipenv``` first e.g.

```markdown
## Local

#### 1. Install pipenv (if not already)

$ pip install --user pipenv

#### 2. Install Dotenv, Pandas, s3Fs and Jupyter

$ pipenv install python-dotenv pandas s3fs jupyter
```

```markdown
## Deepnote

#### 1. Deepnote, by default, uses pip and a requirements.txt file to allow you to install and track additional pacakges. To swap this to pipenv and a Pipfile, copy the code below and replace the existing code cell in your Deepnote Project's init.ipynb file.

%%bash
# If your project has a 'Pipfile' file, we'll install it here apart from blacklisted packages that interfere with Deepnote (see above).
if test -f Pipfile
  then
    sed -i '/jedi/d;/jupyter/d;' Pipfile
    pip install pipenv
    pipenv install --skip-lock
  else
    pip install pipenv
    pipenv install --skip-lock
fi

#### Note: We are skipping the version locking part of the pipenv process (via ```--skip-lock```) because we are not building a long term project and don't want to increase project load times. However, keeping a ```Pipfile.lock``` for long term projects is a must, so make sure you don't ```--skip-lock``` for thoes projects!

#### Note: If project load is awkwardly long, feel free to move ```pip install pipenv``` instructions to ```Dockerfile``` e.g. ```RUN pip install pipenv```. Run build and Restart machine when prompt to do so.

#### 2. Install Dotenv, Pandas and s3Fs via Terminal, or place them in Pipfile (like below) and restart machine.

[packages]
python-dotenv = "*"
pandas = "*"
s3fs = "*"
```

#### ```AWS S3```

> Next up S3! Simple File Storage, at it's simplest. 

1. [Sign Up for AWS Account](https://docs.aws.amazon.com/AmazonS3/latest/gsg/SigningUpforS3.html). 

2. Make sure you [create an IAM user](https://docs.aws.amazon.com/AmazonS3/latest/gsg/SigningUpforS3.html#create-an-iam-user-gsg) and ***copy the credentials (save the .csv)***.

3. [Create a S3 Bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html). Take note of the bucket name.

**Note**: Place it in a ***region*** close to you, e.g. ```eu-west-2```.

#### ```S3 Integration```

> Follow the steps below to integrate S3 into your respective environment. Note that Deepnote users, you can implement either way! If you want to design your notebook to also run locally, follow the stepts to integrate S3 locally.

```markdown
## Local (dotenv, pandas and s3fs)

#### 1. Create .env file within root of your project directory.

#### 2. Place Access Key ID and Secret Access Key of your IAM User within .env file. e.g.

AWS_ACCESS_KEY_ID=ASIB2ACCESSKEY
AWS_SECRET_ACCESS_KEY=sDVjMXSECRETACCESSKEY

#### 3. Import load_dotenv from python-dotenv. Use method load_dotenv() to load .env variables into currrent project environment.

import pandas as pd
import s3fs
from dotenv import load_dotenv
load_dotenv()
  
#### 4. Create S3 Client using s3Fs to interact with your S3 Bucket file system (w/ List S3 bucket files example)

s3 = s3fs.core.S3FileSystem(anon=False)
s3.ls('bucket_name')
```

```markdown
## Deepnote

#### 1. Navigate to Integration Tab (https://docs.deepnote.com/features/integrations) of your Deepnote Project

#### 2. Add Amazon S3 Integration (https://docs.deepnote.com/integrations/aws-s3).

##### Note: Use IAM User Access Key and Security Key you saved in .csv earlier. 
##### Note: Make sure you use the name of the bucket you created ealier.
##### Note: You can call the integration name whatever you'd like e.g. sdsacademys3

#### 3. Once connected, click ```how to use``` to get started.

##### Note: Deepnote integrates data storage services, such as S3, by simply extending them onto your project under the directory path /datasets (it can extend more than one integration). This way, you can simply interact with S3 as if it were a directory within your project.

#### 4. List contents of your S3 Bucket on Notebook

!ls /datasets/sdsacademys3
```

#### ```Running```

> See [```aws_s3_python.py```](./aws_s3_python.py) script or [```aws_s3_deepnote.ipynb```](./aws_s3_deepnote.ipynb) notebook for more ***interaction examples***.

#### ```Contributing```

> See [```contributing.md```](./contributing.md)

