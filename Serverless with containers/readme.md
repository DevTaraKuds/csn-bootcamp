# A Serverless Data Analytics Stack

Building a robust data analytics platform traditionally involves complex infrastructure management. You need to provision servers for your database, set up virtual machines for your dashboarding tool, and manage the connectivity between them. This can be time-consuming, expensive, and difficult to scale. 

This I have tackled these challenges by leveraging a fully serverless stack, demonstrating how to deploy a powerful analytics solution without ever managing a server by deploying a complete data analytics solution using a serverless approach on AWS. 

## What is needed
1. Amazon RDS for PostgreSQL: A fully managed, relational database service that handles all the heavy lifting of database administration.

2. Amazon Fargate: A serverless compute engine that runs our containerized application without requiring us to manage the underlying EC2 instances.

3. Metabase: An open-source business intelligence tool deployed as a containerized image on Fargate, used for creating dashboards and visualizations.

By connecting these three services, we create a scalable, secure, and low-maintenance analytics stack. 

## Skills gained
This project proves my proficiency;
*Understanding and implementing serverless architecture.
* Containerization.
* Relational databases in a cohesive, real-world application.
* Cloud and data engineering. It demonstrates my ability to:


## Prerequisite
* Database Service: Amazon RDS running PostgreSQL.

* Container Service: Amazon ECS with the Fargate launch type.

* Application: Metabase, deployed using its official Docker image.

* Connectivity: A secure network connection is established between the Metabase container and the RDS instance, typically using security groups.

## Getting started
Step 1: Set Up the Database

* Navigate to the RDS service in the AWS console.

* Choose "Create database," select PostgreSQL, and opt for a Free Tier instance.

```Engine: PostgreSQL```

```Template: Free Tier (if eligible)```

```DB instance identifier: any name of your choice```

* Configure a master username and password. Note the database endpoint and port.



Step 2: Create Application Load balancer
* From EC2, select Load Balancers 
* Create Application Load Balancer
``` internet-facing```
``` Listeners: HTTP (port 80)```
```Select 2 public subnets```

* Create a Security group
```Forwarding rule: Port 80```

* Create a new Target group: metabase-tg

``` Name: metabase-tg```
```Target type: IP```
``` Protocol/Port: HTTP / 3000```

* Health check settings:

 ``` Protocol: HTTP```

	```Path: /```

	```Port: traffic port```

	```Healthy threshold: 3```

	```Unhealthy threshold: 5```

	```Timeout: 10s```

	```Interval: 30s```

I used one security group for all three services (RDS, ECS and Loadbalancer), enabling port 3000, 5432, 80, 443 and all traffic from anywhere. (Not the best practice but resolved to this as I had a blcoker)


Step 3: create a task definition

* Go to the ECS service and create a new task definition.

* Set the launch type to "Fargate."

``` Launch type: Fargate```
```Task name: metabase```
```CPU/Memory: 1 vCPU, 3 GB```

* Add a container,
```Image: metabase/metabase:latest```
```Port mapping: 3000```

* Input environmental variables

```MB_DB_TYPE=postgres```
```MB_DB_DBNAME=metabase```
```MB_DB_PORT=5432```
```MB_DB_USER=metabase_user```
```MB_DB_PASS=your_password```
```MB_DB_HOST=your-rds-endpoint.rds.amazonaws.com```

* Configure the environment variables to connect to your RDS instance, including the database name, host, port, username, and password.

Step 4: Create Cluster
* From ECS dashboard, select Clusters 
* Create Cluster
``` Choose: “Networking only (Fargate)”```
``` Name it: name of your choice```


Step 5: Create service

* From the cluster we have just created

* Create service

```Launch type: Fargate```
``` Task Definition: newtask family```
```Service name: metabase-service```
``` Number of tasks: 1```
``` VPC: Same as your RDS and LB```
``` Subnets: Select 2 public subnets```
``` our security group```

* Enable Load Balancer integration:
```Type: Application Load Balancer```
``` Listener: HTTP 80```
``` Target Group: metabase-tg```

Step 6: Deploy Service

Step 7: Launch secured DNS
* Go Load Balancer, 
* copy the DNS name of our service 
*open in a new browser tab


That is all.
