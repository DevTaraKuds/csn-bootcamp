# Event-Driven Automation - Triggering a Lambda Function from an S3 Upload

In modern cloud applications, we often need to automate tasks based on events. For example, when a new file is uploaded to a storage service, we might want to process it, analyze it, or simply notify an administrator. This project addresses the challenge of building an event-driven workflow by showing how to trigger a serverless function (AWS Lambda) in response to a specific event (a file upload to an S3 bucket). The Lambda function then completes the workflow by logging the event.

## Prerequisite
1.	Amazon S3: A highly scalable object storage service that acts as the data source.
2.	AWS Lambda: A serverless compute service that runs our code in response to the S3 event.
3.	CloudWatch Logs: A monitoring service where the Lambda function will log its activity, providing a complete audit trail.

[View Demo Here](https://youtu.be/nQutkCcc1pQ)

## Skills Shown
⦁	Serverless computing.

⦁	Event-driven architecture.

⦁	Automation 

⦁	Log monitoring.

Don't get board. If you are confused along the way, refer to my [video demo here.](#)

## Deep Dive

Step 1: Create an S3 Bucket

⦁	In the S3 console, create a new bucket. This is where you'll upload your files. 
⦁	Create an empty folder (e.g Images)


Step 2: Create the Lambda Function

⦁	Go to the Lambda console and create a new function.

⦁	Choose Python as the runtime.

⦁	In the code editor, write the function to get the file name from the S3 event and print it to the logs.
[Pyton code can be found here](https://github.com/DevTaraKuds/csn-bootcamp/blob/main/Automation%20with%20Lambda/lambda.py)


Step 3 - Configure Lambda IAM Role

⦁	Your Lambda function needs permissions to access S3 (to read the event).

⦁	Go to the IAM portal, a permission would have been created with the name of your function

⦁	Edit its execution role to add the AmazonS3ReadOnlyAccess.


Step 4: Return to Lambda dashboard to add the S3 Trigger

⦁	In the Lambda function's "Designer" view, click "Add trigger."

⦁	Select S3 as the trigger.

⦁	Choose the bucket you created in Step 1.

⦁	Select the All object create events event type.


Step 5: Test the Workflow

⦁	Upload a new file to your S3 bucket.

⦁	Go to the Lambda function's "Monitor" tab and view the CloudWatch logs to see the print message confirming the upload.

You can now Automate processes, create event-driven workflows and monitor activity. Feeling like a pro yeah? That's right.
