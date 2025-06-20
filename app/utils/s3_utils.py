import boto3


def get_s3_client(): 
    try:
        s3_client = boto3.client('s3')
        return s3_client
    except Exception as e:
        print(f"Error creating S3 client: {e}")
        return None
    
def upload_file_to_s3(bucket_name: str, file_path: str, object_name: str) -> bool:
    s3_client = get_s3_client()
    if not s3_client:
        return False
    
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File {file_path} uploaded to {bucket_name}/{object_name}")
        return True
    except Exception as e:
        print(f"Error uploading file to S3: {e}")
        return False
    
def upload_data_to_s3(bucket_name: str, data: bytes, object_name: str) -> bool:
    s3_client = get_s3_client()
    if not s3_client:
        return False
    
    try:
        s3_client.put_object(Bucket=bucket_name, Key=object_name, Body=data)
        print(f"Data uploaded to {bucket_name}/{object_name}")
        return True
    except Exception as e:
        print(f"Error uploading data to S3: {e}")
        return False
    
def download_file_from_s3(bucket_name: str, object_name: str, file_path: str) -> bool:
    s3_client = get_s3_client()
    if not s3_client:
        return False
    
    try:
        s3_client.download_file(bucket_name, object_name, file_path)
        print(f"File {object_name} downloaded from {bucket_name} to {file_path}")
        return True
    except Exception as e:
        print(f"Error downloading file from S3: {e}")
        return False