from db import messages
from datetime import datetime, timedelta
import uuid
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
from bson.json_util import dumps

from db import users
from db import messages
from db import bot

def create(conn, user, bot):
    room = {
"name" : uuid.uuid4().hex,
"user": user,
"created" : datetime.now(),
"evaluation" : [],
"depreciated" : False,
"evaluation_complete": False, 
"evaluated" : False,
"evaluated_by" : [],
"bot_room" : bot 
}
    conn["rooms"].insert_one(room)
    return room

#---------------------------------------SETTERS----------------------------------------

def assign_user(conn, room_name):
    room_data = conn['rooms'].find_one({
        'name': room_name
    })
    for user in room_data["user"]:
        users.change_room(conn, name=user, go_to_room=room_data["name"])
        users.add_partner(conn=conn, user_name=user, room_name=room_data["name"])


def evaluation_complete_room(conn=None, name=None):
 conn['rooms'].update_one({
        'name': name,
    }, {
        '$set': {
            'evaluation_complete' : True
        }
    })

def evaluated_room(conn=None, name=None):
 conn['rooms'].update_one({
        'name': name,
    }, {
        '$set': {
            'evaluated' : True
        }
    })

def decommission(conn=None, name=None): 
        conn['rooms'].update_one({
        'name': name,
    }, {
        '$set': {
            'depreciated' : True
        }
    })

def add_evaluation(conn=None, name=None, eval=None): 
        conn['rooms'].update_one({
        'name': name,
        'depreciated' : True,
        'evaluation_complete': False, 
        'evaluated' : False,
        }, {
        '$push': {
            'evaluation' : eval
        }
    })


def add_evaluated_by(conn=None, name=None, user_name=None):
        conn['rooms'].update_one({
        'name': name,
        'depreciated' : True,
        'evaluation_complete': False, 
        'evaluated' : False,
        }, {
        '$addToSet': {
            'evaluated_by' : user_name
        }
    })

#---------------------------------------GETTERS----------------------------------------

def check_eval_complete(conn=None,room_name=None): 
    room_data = conn['rooms'].find_one({
        'name': room_name
    })
    if not room_data["bot_room"]:
        if room_data["evaluated_by"] == room_data["user"]: 
            return True
        else: 
            return False
    else: 
        if len(room_data["evaluated_by"])>0:
            return True
        else: 
            return False

def is_bot_room(conn, room_name):
    room_data = conn['rooms'].find_one({
        'name': room_name})
    return room_data["bot_room"]

def get_single_room_data(conn=None, name=None):
    room_data = conn['rooms'].find_one({
        'name': name
    })
    return room_data



def get_user_room(conn, room_name):
    room_data = conn['rooms'].find_one({
    'name': room_name
    })
    result = []
    for user in room_data["user"]:
        found_user = users.get_single_user_data(conn=conn, name=user)
        found_bot = bot.get_bot_data(conn=conn, query={"name" : user})
        if found_user:
            result.append({"name" : found_user["name"], "avatar" : found_user["avatar"]})
        if found_bot:
            result.append({"name" : found_bot["alias"], "avatar" : found_bot["avatar"]})
    return result



def send_room_information(conn, room_name):
    room = get_single_room_data(conn=conn, name=room_name)
    if room: 
        return {"name": room["name"], 
        "depreciated" : room["depreciated"], 
        "evaluation_complete" : room["evaluation_complete"], 
        "evaluated" : room["evaluated"],
        "evaluated_by" : room["evaluated_by"],
        "user" : get_user_room(conn=conn, room_name=room_name)}
    else: 
        return None



def get_all_room_data(conn):
    print(list(conn['rooms'].find()))
    return list(conn['rooms'].find())


def get_active_room_data(conn):
    return list(conn['rooms'].find({
        'depreciated': False,
        'evaluation_complete': False,
        'evaluated' : False,
    }))


def get_evaluating_room(conn):
    return list(conn['rooms'].find({
        'depreciated': True,
        'evaluation_complete': False,
        'evaluated' : False,
    }))


def get_evaluated_room(conn): 
    return list(conn['rooms'].find({
        'depreciated': True,
        'evaluation_complete': True,
        'evaluated' : False,
    }))



def check_messages(conn=None, name=None): 
    message_list = list(messages.get(conn=conn, room=name))
    count = 0
    message_predecessor = {}
    for idx, message in enumerate(message_list): 
        if idx > 0: 
            if message_predecessor['user_name']!=message['user_name']: 
                count += 1
        message_predecessor = message
    return count


