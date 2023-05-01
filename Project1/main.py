import boto3

ec2_client = boto3.client('ec2')

all_available_vpcs = ec2_client.describe_vpcs()
vpcs = all_available_vpcs["Vpcs"]

for vpc in vpcs:
    print(vpc["VpcId"])
    cidr_block_assoc_set = vpc["CidrBlockAssociationSet"]
    for assoc_set in cidr_block_assoc_set:
        print(assoc_set["CidrBlockState"])
