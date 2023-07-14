import boto3
from boto3.dynamodb.conditions import Key
import sys
from pprint import pprint
from Player import add_player
from Player import update_player
from Player import get_data


def query_players(username_group, username, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
    table = dynamodb.Table('Players')
    response = table.query(
            KeyConditionExpression=Key('username_group').eq(
                username_group) & Key('username').eq(username)
            )
    return response['Items']

def transmissable_string(get_all_usernames):
    user_list = ""
    users = get_data(get_all_usernames)
    for usernames in users:
        print("Got data:")
        pprint(usernames)
        item = usernames['coordinates']
        userns = item['nscoord']
        userew = item['ewcoord']
        username = usernames['username']
        userdt = item['date_time']
        user_list = user_list + f"{username}/{userns}/{userew}/{userdt}/"
    return user_list

def database_input(nscoord, ewcoord, query_play):
    get_all_usernames = "EXISTS"
    players = query_players(get_all_usernames, query_play)

    for player in players:
        print(player['username'])
        print("exists")
        update_player(get_all_usernames, query_play, nscoord, ewcoord)

    if (len(players) == 0):
        print("adding")
        new_player = add_player(get_all_usernames, query_play, nscoord, ewcoord)

    return transmissable_string(get_all_usernames)
