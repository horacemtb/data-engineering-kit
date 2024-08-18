1. Pull MinIO Docker image:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/1%20pull%20minio%20docker%20image.png)

2. Create Docker network to establish communication between MinIO and Ni-Fi containers:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/2.1%20create%20docker%20network.png)

3. Run MinIO container:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/2.2%20run%20minio%20container.png)

4. Go to http://127.0.0.1:9001 to access MinIO UI and ensure that MinIO is running correctly, then create a bucket called "nifihw":

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/3%20open%20minio%20ui.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/4%20bucket%20created.png)

5. Run Ni-Fi container:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/5%20run%20nifi%20container.png)

6. Open Ni-Fi UI:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/6%20open%20nifi%20ui.png)

7. Configure ListenHTTP, RouteOnContent, MergeContent and PutS3Object processors:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/7%20configure%20ListenHTTP%20processor.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/8%20configure%20RouteOnContent%20processor.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/9%20configure%20MergeContent%20processor.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/10%20configure%20PutS3Object%20processor.png)

8. Establish relationships between the processors and run them.

9. Write bash script to send a specified number of requests of each type to 127.0.0.1:8081/loglistener:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/12.1%20write%20bash%20script%20to%20send%20requests.png)

10. Run the script by sending 500 error messages and 500 unmatched messages:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/12.2%20execute%20bash%20script.png)

11. You should be able to see 1000 messages pass through the pipeline, with MergeContent outputting two files, each containing 500 requests of each type.

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/11%20pipeline%20running.png)

12. The files are saved to MinIO s3 (below are the screenshots of the file system storing different results):

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/13.1%20minio%20object%20browser.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/13.2%20minio%20unmatched%20examples.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/nifi-load-raw-data/images/13.3%20minio%20error%20examples.png)

13. The output files can be found at: output_files/*