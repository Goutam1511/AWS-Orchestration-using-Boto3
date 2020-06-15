from s3orchestrator import *
from ec2orchestrator import *

aws_access_key_id = <AWS-ACCESS-KEY>
aws_secret_key    = <AWS-SECRET-KEY>
aws_session_token = <AWS-SESSION-TOKEN>

def convert_ova_to_ami(bucket_name, file_name, file_location = ''):
    s3oc  = s3orchestrator(aws_access_key_id, aws_secret_key, aws_session_token)
    ec2oc = ec2orchestrator(aws_access_key_id, aws_secret_key, aws_session_token)
    s3oc.check_and_create_bucket(bucket_name)
    if s3oc.check_if_file_exists(bucket_name, file_name):
        print "File already exists in S3 Bucket. Skipping Upload."
        import_task_id = ec2oc.import_image_from_s3('CloudPeak Workload AMI from OVA',
                                                    bucket_name, file_name)
        print "Initiated Import task with Task ID : " + import_task_id
        imageid = ec2oc.monitor_import_task(import_task_id)
        if imageid != None:
            print "VM Import Successful."

if __name__ == '__main__':
    convert_ova_to_ami('<S3 Bucket Name>', '<OVA Name with Path>')
