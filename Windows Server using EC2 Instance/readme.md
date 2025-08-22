# Launching a Secure Virtual Machine - Windows Server on AWS.

Creating a virtual server is a foundational skill. However, correctly configuring an instance to be both functional and secure requires attention to detail, especially when dealing with specific requirements like a public subnet and a well-defined security group. Here, our Windows Server 2022 instance on Amazon EC2 will ensure it meets all specified operational and security parameters.

## Project Overview
I outline the process of launching a Windows Server 2022 Core Base AMI in a public subnet, secured with a dedicated security group that only allows inbound RDP access via port 3389. 

## Skills Highlight
* Internet Protocol (RDP, SSH)
* Internet gateway
* Firewall rule (Inbound and Outbound rules)
* Proficiency in AWS EC2.
* Networking and Security configurations.
Configure network resources, including subnets and security groups, to meet specific security requirements.

In summary, this project highlights my practical expertise in cloud infrastructure management. Navigate and utilize the AWS Management Console effectively. Apply the principle of least privilege by restricting inbound access to only the necessary port (3389).



## Prerequisite
1. Configured VPC (usually there is a default VPC created with an AWS account. If you have configured another for your self you can use this too).

2. A Subnet as the instance is deployed in a public subnet.

3. A security group with inbound rules to protect our instance. This can be created during instance configuration

## Let's Dive In
Step 1: Navigate to the EC2 Dashboard
Log in to your AWS account and go to the EC2 service.

Step 2: Launch Instance Wizard 
Click the "Launch instance" button to begin the configuration process.

Step 3: Choose an AMI
In the "Application and OS Images (Amazon Machine Image)" section, search for "Windows Server 2022 Core Base AMI" and select the appropriate one.

Step 4: Choose an Instance Type
Select a suitable instance type (e.g., a t2.micro is usually a good choice for the free tier).

Step 5: Create a Key Pair
Create a new key pair or select an existing one. It is critical to download and save the private key file (.pem or .ppk) in a secure location. You will need this to connect to the instance.

Step 6: Configure Network Settings

* In the "Network settings" section, ensure the VPC is correct.

* Select a public subnet from the dropdown menu.

* Confirm that "Auto-assign public IP" is set to "Enable" to ensure your instance is reachable from the internet.

* Create a Security Group if you haven't yet done so.

> Choose to "Create security group."

> Give it a descriptive name.

> Under "Inbound security group rules," add a new rule:

> Type: RDP

> Source: My IP (this automatically populates your current public IP address for secure access) or a custom range if needed. Just a security measure to restrict access to the server only to your IP address.

or choose from an existing ones

Step 7: Configure Storage
Leave the default storage settings unless you have specific requirements.

Step 8: Leave all other settings as their default value

Step 9: Review and Launch: Review all your settings on the final page and click "Launch instance."

The instance will take a few minutes to initialize. Once the "Instance state" changes to "Running" and the "Status check" shows "2/2 checks passed," you are ready to connect.

Final Steps
Once the instance is running, you can connect to it using an RDP client. Click "Connect" on the EC2 instance dashboard and follow the instructions to get the password and log in. 

[Here](https://youtu.be/VOOX6SRNcak) is a video to work you through the process.


Enjoy your Virtual Machine.
