#print all movies released before 2000
from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

def scan_movies(max_year, display_movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Movies')

    response = table.scan(FilterExpression=Key('year').lt(max_year));
    data=response['Items']
    display_movies(data)
    while 'LastEvaluatedKey' in response:
        response = table.scan(FilterExpression=Key('year').lt(max_year), ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
        display_movies(data)

    return data

if __name__ == '__main__':
    def print_movies(movies):
        for movie in movies:
            pprint(movie)

    max_year = 2000
    print(f"Scanning movies released before {max_year}...")
    scan_movies(max_year, print_movies)
