import boto3
import json


''' Check availabe S3 buckets '''
# s3=boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)

''' Use AWS Comprehend services to retrive the dominant entities from the file and process the text '''

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

data_dict = {}

# This function retrives and update the entities in data_dict
def entity_data(val):
  json_str = json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
  data = json.loads(json_str)
  for val in data['Entities']:
    data_dict.setdefault(val['Type'],[]).append(val['Text'])

# This function retrives and update the KeyPhrases in data_dict
def KeyPhrases_data(val):
  json_str = json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
  data = json.loads(json_str)
  for val in data['KeyPhrases']:
    data_dict.setdefault('KeyPhrases',[]).append(val['Text']) 
  
# This function retrives and update the Sentiment in data_dict
def Sentiment_data(val):
  json_str = json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
  data = json.loads(json_str)
  data_dict.setdefault('Sentiment',[]).append(data['Sentiment'])  

# This is main function will parse the data from the file and send to respetive funciton to retrieve the key data 
print('Calling Detect Entities')
with open('entities.data','r') as file:
      for text in file:
        entity_data(text)
        KeyPhrases_data(text)
        Sentiment_data(text)
print(data_dict)
print('End of Detect Entities')

# Retrive the entities with LanguageCode 'spanish'
# print('Calling Detect Entities')
# with open('spanish.data','r') as file:
#     for text in file:
#         text=text.strip()
#         print(json.dumps(comprehend.detect_dominant_language(Text=text), sort_keys=True,indent=4))
#         #print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='es'), sort_keys=True, indent=4))

# print('End of Detect Entities')

#json_str =json.dumps(comprehend.detect_dominant_language(Text=text), sort_keys=True,indent=4)
        # data = json.loads(json_str)
        #print(data)
        #l = []
        # for val in data['Entities']:
        #   #   if val['Type'] in data_dict :
        #   #       data_dict[val['Type']].append(val['Text'])
        #   #   else:
        #   #       l.insert(0,(val['Text']))
        #   #       data_dict[val['Type']] = l
        #   data_dict.setdefault(val['Type'],[]).append(val['Text'])
        