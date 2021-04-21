# LoCobSS-text-profanity
Setup tested and deployed on Google Cloud Run

## Local Setup
.env file
```
GOOGLE_APPLICATION_CREDENTIALS=
```
see: https://cloud.google.com/docs/authentication/production

Install requirements using `requirements.txt`.

## Deployment
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT/BUILD_NAME
gcloud run deploy --image gcr.io/YOUR_PROJECT/BUILD_NAME --platform managed
```

## Running local batch
If you already have a lot of text and you want to process it, before setting up the cloud service. The `batch.py` file allows you to process a text file. Each text-snippet should be line-sepparated. The output is a json-nd file with corresponding line-separated output. Call it like this:

```bash
python batch.py YOUR_TEXTFILE.txt OUTPUT_FILE.json-nd
```

## Word by Word comparison based on dictionaries

### Python
- https://github.com/areebbeigh/profanityfilter (Deep search does not work)

### NodeJS
- https://github.com/d-oliveros/profanity-censor
- https://www.npmjs.com/package/bad-words
- https://github.com/thisandagain/washyourmouthoutwithsoap

## Machine Learning and others

### Python
- https://github.com/Hironsan/HateSonar (not much better than word-comparison)

## Datasets

- https://www.freewebheaders.com/full-list-of-bad-words-banned-by-google/
- https://github.com/turalus/encycloDB
- https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words
- https://gist.github.com/jamiew/1112488
- https://github.com/chucknorris-io/swear-words
- https://github.com/ani10030/bad-words-detector/find/master
- https://github.com/birgernass/german-insults/blob/master/src/index.json
- https://github.com/pdrhlik/sweary

## Commercial APIs

- https://hatebase.org/about