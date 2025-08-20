# Deploying a Containerized Grafana Instance with Fargate

Modern applications rely on containerization for scalability and efficiency. This is very helpful in terms of producing a Platform As A Service (PAAS) solution. However, managing the underlying infrastructure for these containers can be complex and time-consuming. This project addresses the challenge of deploying a containerized application, without the need to provision or manage servers. AWS Fargate, a serverless compute engine for containers, which simplifies deployment and automates infrastructure management.

## Skills

1. Serverless Computing
2. Containerization
3. PAAS Deployment
4. Automation
5. Cloud Operation and DevOps
6. Network security

## What we'll do

Leverage the official Grafana Docker image from Docker Hub, this project demonstrates a streamlined, serverless deployment process. The configuration ensures secure network access by creating a dedicated security group that allows inbound traffic on port 3000, which is the default port for Grafana. This project highlights my practical experience with containerization, serverless technologies, and cloud security.


## Here we go.

Step 1: Create a Task Definition:

In the ECS dashboard, navigate to "Task Definitions."

* Click "Create new task definition."

* Choose "Fargate" as the launch type.

* Add a container, providing the image name: grafana/grafana.

* Specify the port mapping for Grafana as 3000.

Step 2: Create a Cluster:

* Go to the "Clusters" section and create a new cluster.

* Choose the "Networking only" template (as Fargate manages the compute).

Please note, configure step 1 before two, it will still produce same result.

Step 3: Create the Service:
* Navigate to the new cluster and click on the "Services" tab.

* Click "Create" and select the task definition you created.

* Choose "Fargate" as the launch type.

* Configure your network settings: select a VPC and at least one public subnet.

* Configure the Security Group:

> During the service creation, you will need to create a new security group or use an existing one.

> Add an inbound rule to this security group:

> ``` Type: Custom TCP ```

> ``` Protocol: TCP ```

> ``` Port Range: 3000 ```

> ``` Source: Your IP address or a specific CIDR range to restrict access.```

Step 4: Launch and Verify to complete the service creation.

Step 5: Once the service is running, find the public IP address or DNS name of the running task.

Open a web browser and navigate to http://<public-ip-address>:3000 to access the Grafana dashboard.

Watch My [Video Demonstration](#)

Serverless cloud capabilities help you to deploy and manage applications efficiently and securely. Enjoy.
