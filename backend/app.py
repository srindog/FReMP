from flask import Flask, redirect, url_for
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from pymongo import MongoClient
import json
import os
from constants import *

load_dotenv()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

client = MongoClient(
  os.getenv('DB_URI'), 
  tls=True, 
  tlsCertificateKeyFile=os.getenv('DB_CERT_FILE_PATH')
)
test_db = client['testDB']
test_col = test_db['testCol']

@app.route('/greeting')
def greeting():
  return {'greeting': GREETING}

@app.route('/greeting/mongo')
def mongo_greeting():
  mongo_greeting = test_col.find_one({'greeting': 'Hello from Mongo!'})
  return {'greeting': mongo_greeting['greeting']}


if __name__ == "__main__":
  app.run(debug=(True if os.getenv('FLASK_DEBUG') == 'true' else False))