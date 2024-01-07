import boto3
from typing import List
from cloudpathlib import S3Path
import pandas as pd

def get_bucket_uri_by_keyword(keyword: str) -> List[str]:
    
    s3_client = boto3.client("s3")
    
    response = s3_client.list_buckets()
    
    bucket_dict_list = response["Buckets"]
    
    
    bucket_names = [bucket_dict["Name"] for bucket_dict in bucket_dict_list]
    filtered_bucket_names =[ name for name in bucket_names if keyword in name]
    
    return filtered_bucket_names
    
buckets = get_bucket_uri_by_keyword("sagemaker-us")
print(buckets)
bucket_name = buckets[0]
print(bucket_name)

s3_client = boto3.client("s3")
s3_client.download_file(bucket_name, 'meuh.txt', 'meuh.txt')
#s3_client.download_file(bucket_name, 'path/to/file.csv', 'file.csv')

input_path_uri = S3Path(f"s3://{bucket_name}") / 'meuh.txt'
print(f"found file: {input_path_uri.exists()}")
pd.read_csv(input_path_uri)