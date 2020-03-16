#!/bin/python
from locust import HttpLocust, TaskSet, between, events
from locust.clients import HttpSession
import time
import os
from itertools import cycle
import random
import requests
from requests import Request, Response
from requests.auth import HTTPBasicAuth
from requests.exceptions import (InvalidSchema, InvalidURL, MissingSchema,
                                 RequestException)
#from locust.client import ResponseContextManager, LocustResponse
from gevent.lock import Semaphore
from urllib.parse import urlparse, urlunparse
from locust.clients import HttpSession

# 
# all_locusts_spawned = Semaphore()
# all_locusts_spawned.acquire()

# def on_hatch_complete(**kw):
#     all_locusts_spawned.release()

# events.hatch_complete += on_hatch_complete

def makemesleep():
    time.sleep(random.randint(1,3))
    return True

def login(l):
    l.client.get("/login")
    l.client.post("/login", {"username":"ellen_key", "password":"education"})

def logout(l):
    l.client.get("/logout")

def index(l):
    l.client.get("/")


def page404(self):
        self.client.get("/does_not_exist")



def speciala(l):
    l.client.get("/")
    makemesleep()
    l.client.get("/about/")
    makemesleep()
    pass


# class UserBehavior(TaskSet):
#     tasks = [ 
#         index, speciala, page404, login
#     ]

class UserBehavior(TaskSet):
    tasks = [ 
        speciala
    ]

    # def on_start(self):
    #     # all_locusts_spawned.wait()
    #     # self.wait()
    #     login(self)

    # def on_stop(self):
    #     logout(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1.0, 3.0)
    host = "https://google.com"