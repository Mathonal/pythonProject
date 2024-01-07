import boto3
from typing import List

def get_bucket_uri_by_keyword(keyword: str) -> List[str]:
    
    s3_client = boto3.client("s3")
    
    response = s3_client.list_buckets()
    
    bucket_dict_list = response["Buckets"]
    
    
    bucket_names = [bucket_dict["Name"] for bucket_dict in bucket_dict_list]
    filtered_bucket_names =[ name for name in bucket_names if keyword in name]
    
    return filtered_bucket_names
    
bucket_name_list = get_bucket_uri_by_keyword("sagemaker-us")
print(bucket_name_list)
bucket = bucket_name_list[0]
print(bucket)

s3_client = boto3.client("s3")
s3_client.download_file(bucket, 'meuh.txt', 'meuh.txt')