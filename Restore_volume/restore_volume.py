import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')

instance_id = "???"

volumes = ec2_client.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [instance_id]
        }
    ]
)

instance_volume = volumes['Volumes'][0]

snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self'],
    Filters=[
        {
            'Name': 'volume-id',
            'Values': [instance_volume['volumeId']]
        }
    ]
)

latest_snapshot = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)[0]

new_volume = ec2_client.create_volume(
    SnapsotId=latest_snapshot['SnapshotId'],
    AvailabilityZone="eu-central-1b",
    TagSpecifications=[
        {
            'ResourceType': 'volume',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'prod'
                }
            ]
        }
    ]
)

ec2_resource.Instance(instance_id).attach_volume(
    VolumeId=new_volume['VolumeId'],
    Device='/dev/xvdb'
)