# S3 -> Glue -> S3  

An ETL pipeline integrating Amazon S3, Amazon Glue and Spark.


## Project Description

1. CSV files from local is uploaded to S3 bucket.
2. Crawler is setup for S3.
3. Data is read through spark glue context.
4. Data is transformed and loaded back into S3.

## Resources:
1. AWS

## Images

<p align="center">
  <img src="https://github.com/Pranjal-Tripathi-01/AWS/blob/main/Glue/Screenshot%20from%202023-07-31%2021-41-30.png"  title="S3 bucket"> 
  <img src="https://github.com/Pranjal-Tripathi-01/AWS/blob/main/Glue/Screenshot%20from%202023-07-30%2021-10-48.png"  title="Glue job runs">  
  <img src="https://github.com/Pranjal-Tripathi-01/AWS/blob/main/Glue/Screenshot%20from%202023-07-30%2020-54-02.png"  title="cloudwatch log before incremental data load">
  <img src="https://github.com/Pranjal-Tripathi-01/AWS/blob/main/Glue/Screenshot%20from%202023-07-30%2020-54-16.png" title="cloudwatch log after incremental data load">

</p>
