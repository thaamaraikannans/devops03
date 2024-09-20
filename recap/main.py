import boto3
import json
regions = ["ap-south-1", "us-east-1", "ap-southeast-1"]

# regions = "ap-south-1"


def create_email_iden(email):
    try:
        for region in regions:
            ses = boto3.client("sesv2", region_name = region)
            create_email = ses.create_email_identity(
                EmailIdentity=email)
            print(create_email)
        return
    except Exception as err:
        print("you have error in ----->>>>", err)
        return

# create_email_iden("thegreatdenis23@gmail.com")


def create_temp():
    try:
        mail = open("mail.html", "r").read()
        # print(mail)
        ses = boto3.client("sesv2", region_name = "ap-south-1")
        template = ses.create_email_template(
                TemplateName='friday-trip',
                TemplateContent={
                    'Subject': 'Welcome to Trip!',
                    'Text': 'Holiday',
                    'Html': mail
                }
            )
        
    except Exception as err:
        print(err)
        

# create_temp()



def send_email():
    try:
        ses = boto3.client("sesv2", region_name = "ap-south-1")
        send = ses.send_email(
            FromEmailAddress = "thegreatdenis23@gmail.com",
            Destination={
                    'ToAddresses': ['thaamaraikannans.xbi4@gmail.com',]},
            Content = {
                'Template': {
            'TemplateName': 'friday-trip',
            'TemplateData': json.dumps({"data":"nothing"}),
        }
    }
        )
        print(send)
        return
    except Exception as err:
        print(err)
        return

send_email()