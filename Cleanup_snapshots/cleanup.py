import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name="eu-central-1")

snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self']
)

sorted_by_date = sorted(snapshots['Snapshots'], key=itemgetter('StartTime'), reverse=True)

for snap in snapshots['Snapshots']:
    print(snap['StartTime'])

for snap in sorted_by_date:
    print(snap['StartTime'])

for snap in sorted_by_date[2:]:
    ec2_client.delete_snapshot(
        SnapshotId=snap['SnapshotId']
    )
