from flask import Flask, redirect, url_for
from flask_cors import CORS, cross_origin
import json
from pymongo import MongoClient
from dotenv import load_dotenv
import os

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

@app.route('/local_hello')
def hello():
  return {"local_message": "Hello World"}

@app.route('/dynamic_hello')
def dynamic_greeting():
  dynamic_greeting = test_col.find_one({"greeting": "Hello World"})
  return {"message_from_mongo": dynamic_greeting['greeting']}



if __name__ == "__main__":
  app.run(debug=(True if os.getenv('FLASK_DEBUG') == 'true' else False))