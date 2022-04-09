from datetime import datetime
from bson.objectid import ObjectId
from db import messages


def connect(conn=None, name=None, request=None):

    conn['users'].update_one({
        'name': name,
    }, {
        '$set': {
            'sid' : request.sid
        }
    })


def get_single_user_data(conn=None, name=None):
    user_data = conn['users'].find_one({
        'name': name
    })

    return user_data

def get_room_users(conn=None, room=None):
    room_data = conn['users'].find({
        'room': room,
    })
    return room_data



def add_partner(conn, user_name, room_name): 
    room_data = conn['rooms'].find_one({
        'name': room_name
    })
    if room_data["bot_room"]: 
         conn['users'].update_one({'name': user_name}, {'$push': {'past_partners': "Bot"}})
    else: 
        for user in room_data["user"]:
            if user!=user_name:
                conn['users'].update_one({'name': user_name}, {'$push': {'past_partners': user}})
            

def change_room(conn, name, go_to_room):
    conn['users'].update_one({
        'name': name,
    }, {
        '$set': {
            'room': go_to_room,
        }
    })



