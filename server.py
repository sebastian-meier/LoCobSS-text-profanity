from flask import Flask
from flask_restful import Api, Resource, reqparse

from profanityfilter import ProfanityFilter
pf = ProfanityFilter()

from hatesonar import Sonar
sonar = Sonar()

import six
from google.cloud import translate_v2 as translate
import html

from dotenv import load_dotenv
load_dotenv()

APP = Flask(__name__)
API = Api(APP)

class Predict(Resource):

    @staticmethod
    def post():
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

API.add_resource(Predict, '/predict')

if __name__ == '__main__':
  APP.run(debug=True, port='1080')