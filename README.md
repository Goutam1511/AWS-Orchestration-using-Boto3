# AWS-Orchestration-using-Boto3

This repository contains some crude scripts (No Exception handling, no parameterization, no beautification, just functionalities) for creating an AWS EC2 instance from an OVA or custom AMI along with the required resources - Gateways, VPC, Subnet, Route Tables, Security groups, etc using Boto3 script.

The "Convert OVA to AMI" directory contains some scripts to convert an OVA to AMI from scratch. Run the "imageconversion.py" script to convert an OVA to AMI. The full path to OVA file and name of a S3 bucket must be provided inside the script as hardcoding.
The script takes an OVA from the path specified and a S3 bucket name as hardcoding, then checks if the bucket is already present. If not present creates it else checks if the OVA file is already present. If not present, then uploads the OVA. Else it skips uploading the file and directly jumps onto import of AMI from OVA. It creates the import task and constantly monitors the task and when the conversion is finished, it prints the AMI ID as the output.

The OVA to AMI Conversion has some prerequisites that have been detailed into the "Notes" directory.

The "ec2instanceorchestrator.py" script 
