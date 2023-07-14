import boto3
from boto3.dynamodb.conditions import Key
import sys
from botocore.exceptions import ClientError
from datetime import datetime

def add_player(username_group, username, nscoord, ewcoord, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Players')
    response = table.put_item(
            Item={
                'username_group': username_group,
                'username': username,
                'coordinates': {
                    'nscoord': nscoord,
                    'ewcoord': ewcoord,
                    'date_time': str(datetime.now())
                    }
                }
            )
    print("Player added")
    return response


def update_player(username_group, username, nscoord, ewcoord, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Players')
    response = table.update_item(
            Key={
                'username_group': username_group,
                'username': username
                },

            UpdateExpression="set coordinates.nscoord=:n, coordinates.ewcoord=:e, coordinates.date_time=:d",
            ExpressionAttributeValues={
                ':n': nscoord,
                ':e': ewcoord,
                ':d': str(datetime.now())
                },
            ReturnValues="UPDATED_NEW"
            )
    print("Player updated")
    return response


def get_data(username_group, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        table = dynamodb.Table('Players')
        response = table.scan(
                FilterExpression=Key('username_group').eq(username_group)); 
        data = response['Items']

        while 'LastEvaluatedKey' in response:
            response = table.scan(FilterExpression=Key('username_group').eq(username_group), ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])
        return data
