import boto3
from boto3.dynamodb.conditions import Key
import sys
from botocore.exceptions import ClientError


def add_hardware (hardware_id, name, value, dynamodb=None):

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Hardware')
    if (name == 'button'):
        response = table.put_item(
                Item={
                    'hardware_id': hardware_id,
                    'elements': {
                        'button': name,
                        }
                    }
                )
    elif (name == 'switch'):
        response = table.put_item(
                Item={
                    'hardware_id': hardware_id,
                    'elements': {
                        'switch': name,
                        }
                    }
                )
    elif (name == 'rotate'):
        response = table.put_item(
                Item={
                    'hardware_id': hardware_id,
                    'elements': {
                        'rotate': name,
                        }
                    }
                )
    else:
        response = ""
    print("Hardware added")
    return response

def update_hardware(hardware_id, name, value, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Hardware')
    if (name == 'button'):
        response = table.update_item(
                Key={
                    'hardware_id': hardware_id
                    },
                UpdateExpression="set elements.button=:b",
                ExpressionAttributeValues={
                    ':b': value
                    },
                ReturnValues="UPDATED_NEW"
                )
    elif (name == 'switch'):
        response = table.update_item(
                Key={
                    'hardware_id': hardware_id
                    },
                UpdateExpression="set elements.switch=:s",
                ExpressionAttributeValues={
                    ':s': value
                    },
                ReturnValues="UPDATED_NEW"
                )
    elif (name == 'rotate'):
        response = table.update_item(
                Key={
                    'hardware_id': hardware_id
                    },
                UpdateExpression="set elements.rotate=:r",
                ExpressionAttributeValues={
                    ':r': value
                    },
                ReturnValues="UPDATED_NEW"
                )

    else:
        response = ""
    print("Hardware updated")
    return response


def get_data(hardware_id, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Hardware')
    try:
        response = table.get_item(Key={'hardware_id': hardware_id})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        try: 
            return response['Item']
        except:
            return "null"
