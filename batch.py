import logging
logging.basicConfig()
logging.root.setLevel(logging.ERROR)

from profanityfilter import ProfanityFilter
pf = ProfanityFilter()

from hatesonar import Sonar
sonar = Sonar()

import sys

import json

# load text file
textfile_path = sys.argv[1]
textfile = json.load(open(textfile_path, "r"))

results_description = []
results_question = []
resultsfile_path = sys.argv[2]

# run profanity check on each line
for text in textfile:
  results_question.append(json.dumps({
    'profanityfilter': pf.is_profane(text['question_en'][0]),
    'sonar': sonar.ping(text=text['question_en'][0])
  }))

  description = ''
  if 'description_en' in text:
    description = text['description_en'][0]
  if 'description_alt_en' in text:
    description = text['description_alt_en'][0]

  if description != '':
    results_description.append(json.dumps({
      'profanityfilter': pf.is_profane(description),
      'sonar': sonar.ping(text=description)
    }))
  else:
    results_description.append(json.dumps({
      'profanityfilter': False,
      'sonar': False
    }))
    

# export as json-nd
with open(resultsfile_path + '/questions-profanity.json-nd', "w") as outfile:
  outfile.write("\n".join(results_question))

with open(resultsfile_path + '/descriptions-profanity.json-nd', "w") as outfile:
  outfile.write("\n".join(results_description))
