# Monitoring a Container with CloudWatch

Deploying a containerized application with serverless technology like AWS Fargate simplifies operations, but it also creates a challenge for monitoring. Without access to the underlying servers, it's not always obvious how your application is performing or if it's consuming too many resources. This project addresses the critical need for visibility by demonstrating how to deploy a container on Fargate and set up a custom CloudWatch Dashboard to monitor its performance in real time. I will deploying a container on Amazon ECS with Fargate and integrating it with AWS CloudWatch for real-time monitoring focusing on two crucial metric CPUUtilization and MemoryUtilization. 

## Skills
* This showcases my ability to not only deploy applications using modern, serverless technology but also to establish a robust monitoring and observability framework, a critical skill in maintaining reliable cloud services.

* Practical experience in a fundamental area of DevOps and cloud engineering: monitoring and observability. It demonstrates my ability to:

* Understanding of how these services work together in the AWS ecosystem.

* Proactive monitoring for any application. By setting up a dashboard, I prove my commitment to operational excellence.

* Analyze Performance Metrics: Focusing on CPU and memory utilization shows a clear understanding of the key indicators of application health.

## Lets Dive In

STEP 1 : Launch a service in ECS
* Create a new ECS Task Definition for your containerized application (e.g., a simple web server).

* Set the launch type to Fargate and ensure the task is configured to use a public subnet.

* Deploy the service, ensuring it runs at least one task.

Step 2 : Create a Dashboard in CloudWatch
⦁	In the AWS Management Console, go to the CloudWatch service.
⦁	In the navigation pane, select "Dashboards" and click "Create dashboard."

> Give it a name, such as ECS-Fargate-Monitoring.

⦁	Add Widgets for Monitoring

> Click "Add widget" and select "Line."

⦁	Choose the ECS namespace.

⦁	Under "Metric Name," search for and select CPUUtilization and MemoryUtilization.

⦁	Filter the metrics by your cluster and service to ensure you are monitoring the correct resources.

⦁	Configure the widget to display the data in a clear, easy-to-read format.

View the [Video demo here.](#)

There goes a live dashboard that provides real-time insights into your application's performance, proactively managing its health and optimize resource usage.
