import boto3

# AMI_ID = (str(input("Enter the Instance ID: ")))
# Instance_Numbers = (int(input("Enter the Number of the Instnces: ")))
AMI_ID = str()
Instance_Numbers = int()
# print(AMI_ID,Instance_Numbers)
# ami-0a261c0e5f51090b1
# Access_Key = (str(input("Enter the Access Key: ")))
# Secret_Key = (str(input("Enter the Secret Key: ")))
Access_Key = str()
Secret_Key = str()
ec2 = boto3.resource('ec2',region_name = "eu-central-1",aws_access_key_id = Access_Key, aws_secret_access_key = Secret_Key)
instances = ec2.create_instances(
        ImageId= AMI_ID,
        MinCount=Instance_Numbers,
        MaxCount=Instance_Numbers,
        InstanceType="t2.micro",
        KeyName="Key_pair_Anbu",
        SecurityGroupIds=[ 'sg-003603580b84ab33e', ],
        SubnetId='subnet-074b1610578134cdb'
#         BlockDeviceMappings=[
#         {
#                 'DeviceName': '/dev/xvda',
#                  'Ebs': {
#                          'VolumeSize': 20,
#                         'VolumeType': 'gp2' }, },],
    )
