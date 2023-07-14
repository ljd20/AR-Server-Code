import boto3

def delete_player_table(dynamodb=None):
	if not dynamodb:
		dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

	table = dynamodb.Table('Players')
	table.delete()

if __name__ == '__main__':
	delete_player_table()
	print("Player table deleted.")
