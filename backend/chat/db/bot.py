import uuid
from db import users

def create(conn, user):

    avatar = {"topValue": "LongHairStraightStrand",
        "skinColorValue":"Pale",
        "accessoriesValue":"Prescription02",
        "hairColorValue":"Blonde",
        "facialhairTypeValue": None,
        "eyeTypeValue":"Squint",
        "eyebrowValue":"Default",
        "mouthValue":"Twinkle",
        "facialHairColorValue":None,
        "clotheTypeValue":"Hoodie",
        "clotheColorValue":"Blue03",
        "eyeColorValue":"Blue01"}
    bot = {
    "name" : uuid.uuid4().hex,
    "user": user,
    "assigned_room" : None,
    "depreciated" : False,
    "avatar" : avatar,
    "alias" : "Gustav",
    }
    print("created bot!!!!")
    conn["bots"].insert_one(bot)
    return bot

def get_bot_data(conn, query): 
        return conn['bots'].find_one(query)


def send_message(conn=None, name_bot=None, message=None):
    return "Ich bin ein Echo bot:" + message



def assign(conn, bot_name, room_name, user_name):
    room_data = conn['rooms'].find_one({
        'name': room_name
    })
    conn['bots'].update_one({'name': bot_name}, {'$set': {'assigned_room': room_name}})
    users.change_room(conn, name=user_name, go_to_room=room_data["name"])
    users.add_partner(conn=conn, user_name=user_name, room_name=room_data["name"])
