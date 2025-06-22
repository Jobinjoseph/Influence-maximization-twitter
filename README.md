# Influence Maximization on Twitter Graph using MRJob and AWS EMR

## Overview

This project implements an influence maximization algorithm using the Independent Cascade (IC) model on a large Twitter follower graph. It leverages MRJob to run MapReduce jobs locally or on an AWS EMR cluster for scalable processing.

## Files

- `influence_max_mrjob.py`: MRJob script implementing the influence maximization.
- `candidate_seeds.txt`: List of candidate nodes to evaluate.
- `twitter-2010.txt.gz`: Twitter follower graph dataset.
- `run_emr_job.py`: Python script to automate running the MRJob on AWS EMR.

## Dataset

The Twitter follower graph used in this project is available from Stanford SNAP:

[https://snap.stanford.edu/data/twitter-2010.html](https://snap.stanford.edu/data/twitter-2010.html)

You can download the compressed edge list file (`twitter-2010.txt.gz`) directly from the SNAP website and upload it to your own AWS S3 bucket for processing.

## Setup

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Configure AWS CLI with your credentials.

3. Upload data files to your S3 bucket.

## Running

Run locally for testing:

```bash
python influence_max_mrjob.py candidate_seeds.txt --runner inline --graph twitter-2010.txt.gz
