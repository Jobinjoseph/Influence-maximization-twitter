# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 07:07:06 2025

@author: joseph
"""
import boto3
import os

def upload_file_to_s3(local_file, bucket_name, s3_key):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file, bucket_name, s3_key)
        print(f"Uploaded {local_file} to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Error uploading {local_file}: {e}")

if __name__ == "__main__":
    bucket = 'xxxx'  # your bucket name

    # Files to upload (adjust paths as needed)
    files_to_upload = {
        'influence_max_mrjob.py': 'influence_max_mrjob.py',
        'candidate_seeds.txt': 'candidate_seeds.txt',
        'twitter-2010.txt.gz': 'twitter-2010.txt.gz'
    }

    for local_path, s3_key in files_to_upload.items():
        if os.path.exists(local_path):
            upload_file_to_s3(local_path, bucket, s3_key)
        else:
            print(f"File not found: {local_path}")

