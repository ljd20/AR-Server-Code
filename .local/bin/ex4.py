#print only years and titles of movies starring Tom Hanks
from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key

def get_years_and_titles_of_movies_starring_actor(actor, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

    table = dynamodb.Table('Movies')
    print(f"Get years and titles")

    response = table.query(
            ProjectionExpression="year, title, #info.actors",
            ExpressionAttributeNames={"#info.actors": "actor"},
            KeyConditionExpression=
                Key('info.actors').contains(actor)
    )
    return response['Items']

if __name__ == '__main__':
    actor = 'Tom Hanks'
    print(f"Get years and titles of movies starring {actor}")
    movies = get_years_and_titles_of_movies_starring_actor(actor)
    for movie in movies:
        pprint(movie)
