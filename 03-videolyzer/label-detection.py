# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='lucian63videoanalyzer')
from pathlib import Path
get_ipython().run_line_magic('ls', '/Users/shanlu/Downloads/*.mp4')
pathname = '~/Downloads/production ID_3795655.mp4'
path = Path(pathname).expenduser().resolve()
path = Path(pathname).expanduser().resolve()
print (path)
print(path.name)
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
response = rekognition_client.start_label_detection(Video={})
response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name': path.name}})
print(response)
from pprint import pprint
pprint(response)
job_id = response['JobId']
result = rekognition_client.get_label_detection(JobId=job_id)
result 
result.keys()
result['JobStatus']
result['VideoMetadata']
len(result['Labels'])
