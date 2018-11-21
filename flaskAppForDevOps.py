from flask import Flask, redirect, url_for, request, render_template, flash, jsonify
from flask_restful import Api, Resource, reqparse
import os
from gevent.pywsgi import WSGIServer

import requests
import json

devopsApp = Flask(__name__)
devopsApp.config['SECRET_KEY'] = 'you-will-never-guess'
api = Api(devopsApp)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

@devopsApp.route('/', methods=['GET'])
def home():
    return ('''<h1>BBTS ChatBot API for Context</h1>
        <p>An API for consuming context and creating slots for RocketChatBBTS.</p>
        <p>Send a POST for /api/chatbot/ with the message and the sessionID and the Bot will answer you properly. <p>''')

@devopsApp.route('/devopsget/', methods=['GET'])
def test1():
    print ("API funcionou o GET")
    return ('GET Ok')

@devopsApp.route('/devopspost/', methods=['POST']) 
def test2():
    respostaJson = {'Funcionou!'}
    respostaJsonData = json.dumps(respostaJson, indent=4)
    return respostaJsonData


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 5000), devopsApp)
    http_server.serve_forever()