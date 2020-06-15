'''
A simple script to convert an OVA present in a S3 Bucket to custom AMI.
'''

import boto3

aws_access_key_id = <AWS-ACCESS-KEY-HERE>
aws_secret_key = <AWS-SECRET-KEY-HERE>
aws_session_token = <AWS-SESSION-TOKEN-HERE>

client = boto3.client('ec2', aws_access_key_id = aws_access_key_id,
                      aws_secret_access_key = aws_secret_key,
                      aws_session_token = aws_session_token)

disk_containers = [
        {
            'Description': 'Basic automation attempt',
            'Format': 'ova',
            'UserBucket': {
                'S3Bucket': <S3-BUCKET-NAME-HERE>,
                'S3Key': <OVA-NAME-HERE>
            }
        },
    ]

response = client.import_image(Description = 'Basic try', DiskContainers = disk_containers)

print response
