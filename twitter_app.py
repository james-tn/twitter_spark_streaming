#!/usr/bin/python
# TweetRead.py
import os
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json
import sys


os.environ['SPARK_HOME'] = '/usr/local/spark'
sys.path.append("/usr/local/spark/python")

access_token = 'youraccesstoken'
access_secret = 'youraccesssecret'
consumer_secret = 'yourconsumersecret'
consumer_key = 'yourconsumerkey'

class TweetsListener(StreamListener):
    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            # print(data.split('\n'))
            self.client_socket.send(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True
    # def on_status(self, status):
    #
    #     description = status.user.description
    #     loc = status.user.location
    #     text = status.text
    #     coords = status.coordinates
    #     name = status.user.screen_name
    #     user_created = status.user.created_at
    #     followers = status.user.followers_count
    #     id_str = status.id_str
    #     created = status.created_at
    #     retweets = status.retweet_count
    #     bg_color = status.user.profile_background_color
    #
    #     print(text)
    #     self.client_socket.send(text)


def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    twitter_stream = Stream(auth, TweetsListener(c_socket))
    twitter_stream.filter(track=['trump', 'clinton', 'donald trump', 'US', 'Russia', 'APEC', 'republican', 'Dem', 'Rep', 'gun', 'kill', 'killer', 'church','america'])


if __name__ == "__main__":
    s = socket.socket()  # Create a socket object
    host = "spark1"  # Get local machine name
    port = 5555  # Reserve a port for your service.
    s.bind((host, port))  # Bind to the port

    print("Listening on port: %s" % str(port))

    s.listen(1)  # Now wait for client connection.
    c, addr = s.accept()  # Establish connection with client.

    print("Received request from: " + str(addr))

    sendData(c)