from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

active_user = {'username':'guest',
               'password':''}

from app import routes