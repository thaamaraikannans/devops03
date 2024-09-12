import boto3

def create_ec2():
    ec2 = boto3.resource("ec2", region_name = "ap-southeast-1")
    reponse = ec2.create_instances(
        KeyName='singapore',
    MaxCount=1,
    MinCount=1,
    ImageId = "ami-04a5ce820a419d6da",
    InstanceType = "t3.micro"
    )
    print(reponse)
    return

# create_ec2()

def stop_ec2():
    ec2 = boto3.client("ec2", region_name = "ap-southeast-1")
    response = ec2.describe_instances()
    # print(response)
    instances = response["Reservations"]
    for id in instances:
        stop_ins_id = id["Instances"][0]["InstanceId"]
        data = ec2.stop_instances(InstanceIds=[stop_ins_id])
        print(data)
    return

stop_ec2()