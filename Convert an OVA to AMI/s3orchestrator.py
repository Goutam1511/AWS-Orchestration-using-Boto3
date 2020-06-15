import boto3

class s3orchestrator:
    def __init__(self, access_id, secret_key, session_token):
        self.s3client = boto3.client('s3', aws_access_key_id = access_id,
                                    aws_secret_access_key = secret_key,
                                    aws_session_token = session_token)

    def list_buckets(self):
        response = self.s3client.list_buckets()['Buckets']
        result = []
        for i in response:
            result.append(i['Name'])
        return result

    def is_bucket_present(self, bucket_name):
        if bucket_name in self.list_buckets():
            return True
        return False

    def create_bucket(self, bucket_name):
        self.s3resource = boto3.resource('s3')
        self.s3resource.create_bucket(Bucket = bucket_name)

    def check_and_create_bucket(self, bucket_name):
        if not self.is_bucket_present(bucket_name):
            self.create_bucket(bucket_name)
        else:
            print "Bucket already present. Skipping new Bucket creation."

    def check_if_file_exists(self, bucket_name, file_name):
        results = self.s3client.list_objects(Bucket = bucket_name, Prefix = file_name)
        return 'Contents' in results
