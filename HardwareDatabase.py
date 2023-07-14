import boto3
from boto3.dynamodb.conditions import Key
import sys
from pprint import pprint
from Hardware import add_hardware
from Hardware import update_hardware
from Hardware import get_data


def query_fpga(username, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
    table = dynamodb.Table('Hardware')
    response = table.query(
        KeyConditionExpression=Key('hardware_id').eq(username)
    )
    if len(response) > 0:
        return response['Items']
    else:
        return null
'''if __name__ == '__main__':'''
def database_input(name, value, q_hardware):
    '''nscoord = str(sys.argv[3])  # input from phone
    ewcoord = str(sys.argv[4])  # input from phone
    query_play = str(sys.argv[2])  # input from phone
    socket_status_receiving = int(sys.argv[1])  # sending is 0'''

    hardwares = query_fpga(q_hardware)

    for selected in hardwares:
        print(selected['hardware_id'])
        print("exists")
        update_hardware(q_hardware, name, value)

        send = get_data(q_hardware)
        if send:
            print("Got data:")
            pprint(send)
            if hasattr(send, 'elements'):
                item = send['elements']
                sending = (item[name])
            #sending_switch = (item['switch'])
            #sending_rotated = (item['rotated'])
                return sending
            else:
                return "sending"
            '''print(sending_ns, ":", sending_ew)
            print("date and time: ", sending_date)'''
    if (len(hardwares) == 0):
        print("adding")
        add_hardware(q_hardware, name, value)
        return value

# set up ctcp connection
# wait for the phone to "write to tcp"
# connection_socket.recv().decode()
# add_player(necessary data)
