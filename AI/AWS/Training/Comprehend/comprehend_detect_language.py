import boto3
import json


''' Check availabe S3 buckets '''
s3=boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

''' Use AWS Comprehend services to retrive the dominant language in the text and entities '''
comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
text = 'Quality thought is good institute in Hyderabad'

print('Calling Detect Entities')
#print(json.dumps(comprehend.detect_dominant_language(Text=text), sort_keys=True,indent=4))
print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of Detect Entities')

#mahendrabigdata@gmail.com