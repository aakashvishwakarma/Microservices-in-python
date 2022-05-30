import boto3
import json
s3_client = boto3.client('s3',
    aws_access_key_id='AKIAXQLURLRJVWVPK7HC',
    aws_secret_access_key='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',
    # aws_session_token=SESSION_TOKEN
    )
b=[]
# objects = s3_client.list_objects(Bucket='Bucket/NANI')
response = s3_client.list_objects_v2(Bucket='test12356jsd')
# print(response["Contents"]["Key"])
count= 0
for key in response["Contents"]:
# # # if 'NANI' in key:# print(key) 
    if str.find(str(key),'EBS/') > 1: 
        a=key 
        if count >= 1: 
            b.append(str(a["Key"])) 
        count=count+1
jsonfilesname=[]
for x in range(len(b)): 
    print(b[x])
    jsonfilesname.append(b[x])
    print(jsonfilesname)
result=[]
for key in jsonfilesname:
    data = s3_client.get_object(Bucket='test12356jsd', Key=key)
    content = json.loads(data['Body'].read().decode("utf-8"))
    result.append(content)
# print(json.dumps(result)) # Do something with the merged contentprint(json.dumps(result))
print(json.loads(json.dumps(result)))