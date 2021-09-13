import requests
import json
from types import SimpleNamespace as Namespace

def removeUserWithoutInfo(data, info):
    temp = []
    for i in range(len(data)):
        if hasattr(data[i], info):
            aux = data[i].__dict__[info]

            if(aux != ''):
                temp.append(data[i])

    return temp

def removeUnnecessaryProperty(data):
    for i in range(len(data)):
        if hasattr(data[i], 'image'):
            delattr(data[i],'image')
    return data


def removeUserId(id, data):
    temp = []
    for i in range(len(data)):
        if hasattr(data[i], '_id'):
            if data[i]._id != id:
                temp.append(data[i])
    return temp

def onlyById(id, data):
    temp = []
    for i in range(len(data)):
        if hasattr(data[i], '_id'):
            if data[i]._id == id:
                temp.append(data[i])
    return temp

def showUsers(data):
    for i in range(len(data)):
        print(data[i])