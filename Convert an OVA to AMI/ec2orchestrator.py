import boto3
from time import sleep

class ec2orchestrator:
    def __init__(self, access_id, secret_key, session_token):
        self.ec2client = boto3.client('ec2', aws_access_key_id = access_id,
                                     aws_secret_access_key = secret_key,
                                     aws_session_token = session_token)

    def import_image_from_s3(self, description, bucket_name, file_name):
        self.disk_containers = [
                {
                    'Description': description,
                    'Format': 'ova',
                    'UserBucket': {
                        'S3Bucket': bucket_name,
                        'S3Key': file_name
                    }
                },
            ]
        response = self.ec2client.import_image(Description = description,
                                               DiskContainers = self.disk_containers)
        return response['ImportTaskId']

    def monitor_import_task(self, taskId):
        while True:
            response = self.ec2client.describe_import_image_tasks(ImportTaskIds=[taskId])
            for task in response['ImportImageTasks']:
                if task['ImportTaskId'] == taskId:
                    if 'ImageId' in task.keys():
                        self.imageid = task['ImageId']
                        print "Image ID : " + self.imageid
                    if task['Status'] in ['active', 'converting', 'updating']:
                        print "Import in Progress. Progress : " + task['Progress'] + "% Completed."
                        sleep(40)
                    elif task['Status'] in ['deleted', 'deleting']:
                        print "Import Cancelled. Error! Retry"
                        return None
                    elif task['Status'] == 'completed':
                        print "AMI Ready to Launch Instance. Image ID : " + self.imageid
                        return self.imageid
