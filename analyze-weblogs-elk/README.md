### Credit

This work is based on the https://github.com/Gorini4/elk_demo template, but includes an edited logstash configuration file and screeshots of created visualizations by me

1. Run docker-compose up -d and check that ElasticSearch and Kibana are running in the background:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/analyze-weblogs-elk/images/1.%20run%20docker-compose.png)

2. Check that Kibana is running at localhost:5601

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/analyze-weblogs-elk/images/2.%20Check%20that%20kibana%20is%20running.png)

3. Edit the logstash configuration file so that the data is preprocessed correctly before being loaded into ElasticSearch:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/analyze-weblogs-elk/images/3.%20Edit%20logstash%20file.png)

4. Execute the ./load_data.sh script and make sure the data has been loaded into ElasticSearch:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/analyze-weblogs-elk/images/4.%20Show%20that%20there's%20data%20in%20ElasticSearch.png)

5. Create a weblogs index pattern and specify the "Time_created" column as the time field:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/analyze-weblogs-elk/images/5.%20Weblogs%20index.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/analyze-weblogs-elk/images/6.%20Time_field.png)

6. Make sure the data has appeared in Kibana:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/analyze-weblogs-elk/images/7.%20Show%20data%20in%20Kibana.png)

7. Create a Lens visualization in Kibana and save it as a dashboard:

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/analyze-weblogs-elk/images/8.%20Create%20visualization.png)

![Alt text](https://github.com/horacemtb/data-engineering-kit/blob/main/analyze-weblogs-elk/images/9.%20Save%20dashboard.png)