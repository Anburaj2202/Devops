import boto3
import sys
print(Access_Key,Secret_Key)
ec2 = boto3.client('ec2',region_name = "eu-central-1")
response = ec2.describe_instances()
Reservations = response["Reservations"]
for Reservation in Reservations:
    Instances = Reservation["Instances"]
    for Instance in Instances:
        Instance_ID = Instance["InstanceId"]
        if Instance_ID != "i-0cfae55f456f878ae":
            Instace_VPC = Instance["VpcId"]
            if Instace_VPC == "vpc-0d3298feae5587a44":
                Stop_Instance = ec2.stop_instances(InstanceIds=[Instance_ID,],)
                print("Instance {} has been Stopped".format(Instance_ID))
