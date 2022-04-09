from os import name
from bson.json_util import dumps


import random
import time
from datetime import datetime, timedelta

import random

from db import connection 
from db import messages 
from db import rooms
from db import users
from db import bot

from utils.select import select_random_Ns



def chat_start(mongodb_db):
    start_room_evaluation(mongodb_db)
    end_room_evaluation(mongodb_db)
    room_unassignment(mongodb_db)
    room_assignment(mongodb_db)



def coin_toss(p=.5):
    return True if random.random() < p else False


def create_chatbot(conn=None, user=None):
    chatbot = bot.create(conn=conn,user=user)
    return chatbot


def match_chatbot_with_user(conn=None):
    not_assigned=list(conn["users"].find({'room': None, 'past_partners': { "$nin" : [ "Bot" ]}}, {  "name": 1 }))
    for user in not_assigned: 
        #if coin_toss(): 
        chatbot = bot.create(conn=conn, user=user["name"])
        room = rooms.create(conn=conn, user=[user["name"],chatbot["name"]], bot=True)
        bot.assign(conn=conn, bot_name=chatbot["name"], room_name=room["name"], user_name=user["name"])



def room_assignment(db, n=2):
    match_chatbot_with_user(conn=db)
    not_assigned = list(db['users'].find({'room': None}).sort([('created_at', -1)]))
    print("ALL USER", not_assigned)
    room_user = []
    for room in rooms.get_all_room_data(db): 
        room_user.append(room['user'])
    print("ALL USER", not_assigned)
    print("ROOM USER::::::", room_user)
    assigned = select_random_Ns(not_assigned, room_user)
    roomsHelper = []
    for elem in assigned:
        if len(elem)>1: 
            room = rooms.create(conn=db, user=elem, bot=False)
            roomsHelper.append(room)
    for room in roomsHelper: 
        rooms.assign_user(conn=db, room_name=room["name"])

        
def start_room_evaluation(db): 
    for room in rooms.get_active_room_data(db): 
        if (rooms.check_messages(conn=db, name=room["name"])) > 2:
            rooms.decommission(conn=db, name=room["name"])

def end_room_evaluation(db): 
    for room in rooms.get_evaluating_room(db):
        if rooms.check_eval_complete(conn=db, room_name=room["name"]):
            rooms.evaluation_complete_room(conn=db, name=room["name"])

def room_unassignment(db): 
    for room in rooms.get_evaluated_room(db):
        rooms.evaluated_room(conn=db, name=room["name"])
        for user in room["user"]:
            users.change_room(conn=db, name=user, go_to_room=None)