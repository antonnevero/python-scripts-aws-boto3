import boto3

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

instances = ec2_client.describe_instances()
print(instances)