# coding: utf-8
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2020-05-25T22:24:39.222Z', 'eventName': 'ObjectCreated:CompleteMultipartUpload', 'userIdentity': {'principalId': 'AWS:AIDA3K6QK7MLEP7TPAXCU'}, 'requestParameters': {'sourceIPAddress': '76.224.22.81'}, 'responseElements': {'x-amz-request-id': 'FD22065C4164BCC5', 'x-amz-id-2': 'CJgr95wsyVT15VHxr5CzxuZ725RYaJhek3cP1LwrhEWhxBABflofV4EDwAiyFoOoQCAUECarcAZ4edN+P70v3lZAOpYrvxmT'}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '670a5ea3-6f7c-4f5a-a630-7756e94c5ae4', 'bucket': {'name': 'lucian63videolyzervideos12345', 'ownerIdentity': {'principalId': 'AYPVXF84DDJHU'}, 'arn': 'arn:aws:s3:::lucian63videolyzervideos12345'}, 'object': {'key': 'production+ID_3795655.mp4', 'size': 43287339, 'eTag': '31e03c4443502f461540148365b17f3c-6', 'sequencer': '005ECC459E447A3123'}}}]}
event
event['Records'][0]['s3']['bucket']['name']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
