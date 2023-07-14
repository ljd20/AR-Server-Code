import boto3
from pprint import pprint
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

def create_hardware_table(dynamodb=None):
	if not dynamodb:
		dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
	table = dynamodb.create_table(
		TableName='Hardware',
		KeySchema=[
			{
				'AttributeName': 'hardware_id', #could use IP or which port is >
				'KeyType': 'HASH'
			}
		],
		AttributeDefinitions=[
			{
				'AttributeName': 'hardware_id',
				'AttributeType': 'S'
			},
		],
		ProvisionedThroughput={
			'ReadCapacityUnits': 10,
			'WriteCapacityUnits': 10
		}
	)
	return table

if __name__ == '__main__':
	hardware_table = create_hardware_table()
	print("Table status:", hardware_table.table_status)
