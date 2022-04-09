from pymongo import MongoClient

import os
import configparser


def init_config():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    config = configparser.ConfigParser()
    config.read(f'{dir_path}/config.ini')
    return config


def init_mongodb_conn(config=None):
    if config is None:
        raise SystemExit('Error: need config to know witch database config you will use')

    uri = config['mongodb']['uri']
    database = config['mongodb']['database']



    try:
        client = MongoClient(uri)
        if database:
            db = client[database]
        else: 
            db = client[config['mongodb']['database']]
    except ValueError as e:
        print('MongoDB connection to {host}:{port} is refused')
        print(e)
        raise SystemExit()

    return db, client