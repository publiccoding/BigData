import boto3
import json

# Author : mahendrabigdata@gmail.com

''' Use AWS Comprehend services to retrive the dominant language in the text and entities '''
comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
text = 'Today weather in Hyderabad is very bad, but hyderabad is a good place to visit.'

''' Check availabe S3 buckets '''
# s3=boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)

print('Calling Detect Language')
print(json.dumps(comprehend.detect_dominant_language(Text=text), sort_keys=True,indent=4))
print('End of Detect Language')

print('Calling Detect Entities')
print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of Detect Entities')

print('Calling Detect Phrases')
print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of Detect Key Phrases')

print('Calling Detect Sentiment')
print(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of Detect Sentiment')