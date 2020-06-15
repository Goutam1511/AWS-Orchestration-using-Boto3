# AWS-Orchestration-using-Boto3

This repository contains some crude scripts (No Exception handling, no parameterization, no beautification, just functionalities) for creating an AWS EC2 instance from an OVA or custom AMI along with the required resources - Gateways, VPC, Subnet, Route Tables, Security groups, etc using Boto3 AWS SDK scripting.

#### Requirements :

We are assuming Python 2.7 & PIP package is already present.

1. Install AWS CLI
2. Set up AWS Account and configure AWS Programmatic access using the below command.
   ``` aws configure ```
3. Provide the AWS access credentials, set up JSON output format and set region of AWS account.
4. Install Boto3 using the below command
   ``` pip install boto3 ```

#### Convert OVA to AMI

The "Convert OVA to AMI" directory contains some scripts to convert an OVA to AMI from scratch. Run the "imageconversion.py" script to convert an OVA to AMI. The full path to OVA file and name of a S3 bucket must be provided inside the script as hardcoding.
The script takes an OVA from the path specified and a S3 bucket name as hardcoding, then checks if the bucket is already present. If not present creates it else checks if the OVA file is already present. If not present, then uploads the OVA. Else it skips uploading the file and directly jumps onto import of AMI from OVA. It creates the import task and constantly monitors the task and when the conversion is finished, it prints the AMI ID as the output.

The OVA to AMI Conversion has some prerequisites. To meet them -
1. Create an IAM role named vmimport with proper trust relationships using below command.
   Use the file "trust-policy.json" inside *Notes* folder for this.
   
   ``` aws iam create-role --role-name vmimport --assume-role-policy-document file://trust-policy.json ```

2. Put the permissions in the newly created role from file "role-policy.json" inside *Notes* using below command.

  ``` aws iam put-role-policy --role-name vmimport --policy-name vmimport --policy-document "file://role-policy.json"```

#### Notes

The Notes directory contains some notes that I thought might be useful for manual creation of AWS resources.

#### ec2instanceorchestrator.py

The "ec2instanceorchestrator.py" script orchestrates the creation of an EC2 instance from a custom AMI.
