# -*- coding: utf-8 -*-
"""
@author: joseph
"""

import subprocess

def run_emr_job():
    cmd = [
        "python",
        "influence_max_mrjob.py",
        "s3://xxxx/candidate_seeds.txt",
        "--runner", "emr",
        "--ec2-key-pair", "influence-max-key",
        "--ec2-key-pair-file", "xxxxx/influence-max-key.pem",
        "--region", "eu-north-1",
        "--graph", "s3://xxxx/twitter-2010.txt.gz",
        "--output-dir", "s3://xxxx/output-folder/"
    ]
    # Run the command and wait for it to finish
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    run_emr_job()
