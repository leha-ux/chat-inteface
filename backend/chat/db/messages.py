from datetime import datetime
from db import rooms


def insert(conn=None, user_name=None, room_name=None, text=None):
   room_data = rooms.get_single_room_data(conn=conn,name=room_name)
   if not room_data["depreciated"]:
      conn['messages'].insert_one({
         'user_name': user_name,
         'room_name': room_name,
         'text': text,
         'created_at': datetime.utcnow()
      })

def get(conn=None, room=None, limit=50):
   return conn['messages'].find({
      'room_name': room
   }).sort([('created_at', 1)]).limit(limit)