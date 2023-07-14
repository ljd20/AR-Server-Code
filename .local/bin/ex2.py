#print complete information on movie 'After Hours' released in 1985
import boto3
from boto3.dynamodb.conditions import Key

def get_movie(title, year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

    table = dynamodb.Table('Movies')
    print(f"Get all details")

    response = table.query(
            KeyConditionExpression=
                Key('year').eq(year) & Key('title').eq(title)
    )
    return response['Items']

if __name__ == '__main__':
    query_year = 1985
    query_title = 'After Hours'
    print(f"Get movies from {query_year} with title {query_title}")
    movie = get_movie(query_title, query_year)
    print(movie[0])
