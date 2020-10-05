#########
# AWS S3 and Python (Pandas + S3Fs)
# 
# Pandas Reference: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#reading-remote-files, S3Fs Docs: https://s3fs.readthedocs.io/en/latest/api.html
# 
# 1. [Sign Up for AWS Account](https://docs.aws.amazon.com/AmazonS3/latest/gsg/SigningUpforS3.html). Make sure you create an IAM user and copy the credentials (save the .csv).
# 
# 2. [Create a S3 Bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html). Place it in a region close to you, e.g. eu-west-2.
# 
# S3Fs Integration with Python
# 
# 1. Install [python-dotenv](https://pypi.org/project/python-dotenv/) into your project.
# 
# 2. Create **.env** file within ***root*** of your project directory.
# 
# 3. Place ***Access Key ID*** and ***Secret Access Key*** of your **IAM User** within **.env** file. e.g.
#   
#   AWS_ACCESS_KEY_ID=ASIB2ACCESSKEY
#   AWS_SECRET_ACCESS_KEY=sDVjMXSECRETACCESSKEY
# 
## 4. Import s3fs and load_dotenv. Use method load_dotenv() to load .env variables into currrent project environment. See example below.
##########

import pandas as pd
import s3fs
from dotenv import load_dotenv
load_dotenv()
print('Loaded Env')

# Use s3fs S3FileSystem Client (will use credentials in .env)
s3 = s3fs.core.S3FileSystem(anon=False)
print('Created S3 Client')

print('Fetching Sample Data')
url = 'https://sportsdatasolutionsacademy.s3.eu-west-2.amazonaws.com/data/swimming_psb_data.csv'
df = pd.read_csv(url)
df = df[df['c_NOC'] == 'Great Britain'].drop_duplicates()
print('Filtered GB Athletes')

# Upload (using pandas and s3:// extension)
print('Try Upload')
df.to_csv(r's3://sportsdatasolutionsacademy/data/gb_swimming_psb_data.csv', index=False)

# List (using loop on s3.list output from 'sportsdatasolutionsacademy/data' path)
print('Try List')
for document in s3.ls('sportsdatasolutionsacademy/data'):
    print(document)

# Read (using pandas and s3:// extension)
print('Try Read')
df = pd.read_csv('s3://sportsdatasolutionsacademy/data/gb_swimming_psb_data.csv')
df

# Delete (using s3.rm)
print('Try Delete')
s3.rm('s3://sportsdatasolutionsacademy/data/gb_swimming_psb_data.csv')