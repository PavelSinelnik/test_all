import datetime
import base64
import boto3


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    get_file_content = event['content']

    object = s3.put_object(Bucket="example141323", Key=event['id'], Body=get_file_content)

    db = boto3.client('dynamodb')
    now = datetime.datetime.now()
    db.put_item(
        TableName='data_from_users',
        Item={
            'id': {
                "S": event['id']
            },
            'date': {
                "S": str(now.day) + '.' + str(now.month) + '.' + str(now.year)
            },
            'time': {
                "S": str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + '.' + str(now.microsecond)
            }

        }
    )

    return object['VersionId']