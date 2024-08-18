1. Pull MinIO Docker image:

![Alt text]()

2. Create Docker network to establish communication between MinIO and Ni-Fi containers:

![Alt text]()

3. Run MinIO container:

![Alt text]()

4. Go to http://127.0.0.1:9001 to access MinIO UI and ensure that MinIO is running correctly, then create a bucket called "nifihw":

![Alt text]()

![Alt text]()

5. Run Ni-Fi container:

![Alt text]()

6. Open Ni-Fi UI:

![Alt text]()

7. Configure ListenHTTP, RouteOnContent, MergeContent and PutS3Object processors:

![Alt text]()

![Alt text]()

![Alt text]()

![Alt text]()

8. Establish relationships between the processors and run them.

9. Write bash script to send a specified number of requests of each type to 127.0.0.1:8081/loglistener:

![Alt text]()

10. Run the script by sending 500 error messages and 500 unmatched messages:

![Alt text]()

11. You should be able to see 1000 messages pass through the pipeline, with MergeContent outputting two files, each containing 500 requests of each type.

![Alt text]()

12. The files are saved to MinIO s3 (below are the screenshots of the file system storing different results):

![Alt text]()

![Alt text]()

![Alt text]()

13. The output files can be found at: output_files/*