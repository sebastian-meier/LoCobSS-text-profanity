import logging
logging.basicConfig()
logging.root.setLevel(logging.ERROR)

from flask import Flask
from flask_restful import Api, Resource, reqparse

from profanityfilter import ProfanityFilter
pf = ProfanityFilter()

from hatesonar import Sonar
sonar = Sonar()

import six
from google.cloud import translate_v2 as translate
import html

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route('/')
def root():
  return 'Hello', 200

@app.route('/predict', methods=['POST'])
def predict():
  parser = reqparse.RequestParser()
  parser.add_argument('text')
  args = parser.parse_args()

  text = args["text"]
  
  translate_client = translate.Client()

  if isinstance(text, six.binary_type):
    text = text.decode("utf-8")

  result = translate_client.translate(text, target_language="en")
  text = html.unescape(result["translatedText"])

  out = {
    'profanityfilter': pf.is_profane(text),
    'sonar': sonar.ping(text=text),
    'text': text
  }

  return out, 200

if __name__ == "__main__":
  # use 0.0.0.0 to use it in container
  app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))