import json
import boto3
import zipfile
def lambda_handler(event, context):
    s3=boto3.client('s3')
    l=boto3.client('lambda')
    #key = event["Records"][0]['s3']['object']['key']
   #bucket = event['Records'][0]['s3']['bucket']['name']
    #if key == 'save_device_info.zip':
        #name='save_device_info'
    #if key == 'check_device_info.zip':
        #name = 'check_device_info'
    
    #if name == 'save_device_info' or name == 'check_device_info':
    l.update_function_code(
            FunctionName="check_device_info",
            S3Bucket=forevent,
            S3Key="save_device_info"
                )
    #item = json.dumps(event['Records'][0])
    #object = s3.put_object(Bucket="forevent", Key='tap1.json', Body=item)
    
    return('bydesh havat')
    