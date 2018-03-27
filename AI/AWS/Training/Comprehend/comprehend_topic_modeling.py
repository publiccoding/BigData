import boto3
import json
import bson 



from bson import json_util
 
comprehend = boto3.client(service_name='comprehend', region_name='us-west-2')
                
input_s3_url = "s3://public-sample-us-west-2"
input_doc_format = "ONE_DOC_PER_FILE"
output_s3_url = "s3://comprehendtopicoutput"
data_access_role_arn = "arn:aws:iam::029005890873:role/service-role/AmazonComprehendServiceRoleS3FullAccess-test123"
number_of_topics = 10
 
input_data_config = {"S3Uri": input_s3_url, "InputFormat": input_doc_format}
output_data_config = {"S3Uri": output_s3_url}
 
start_topics_detection_job_result = comprehend.start_topics_detection_job(NumberOfTopics=number_of_topics,
                                                                              InputDataConfig=input_data_config,
                                                                              OutputDataConfig=output_data_config,
                                                                              DataAccessRoleArn=data_access_role_arn)
 
print('start_topics_detection_job_result: ' + json.dumps(start_topics_detection_job_result))
 
job_id = start_topics_detection_job_result["JobId"]
 
print('job_id: ' + job_id)
 
describe_topics_detection_job_result = comprehend.describe_topics_detection_job(JobId=job_id)
 
print(json.dumps(job_id,default=json_util.default))

print('describe_topics_detection_job_result: ' + json.dumps(describe_topics_detection_job_result, default=json_util.default))

list_topics_detection_jobs_result = comprehend.list_topics_detection_jobs()
 
print('list_topics_detection_jobs_result: ' + json.dumps(list_topics_detection_jobs_result, default=json_util.default))
