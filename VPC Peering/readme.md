# VPC Peering for Private Network Communication


On the job, there are occasion where the need to enable secure, private communication between different virtual networks may arise. While an internet gateway allows public traffic, it's not a secure or efficient solution for internal, private-network communication. 

## Overview
VPC peering is a widely used service for connecting services across different accounts, regions, or teams. This addresses the challenge of securely connecting two separate VPCs, demonstrating how to enable seamless and private traffic flow between them.

In creating a private network connection between two distinct VPCs using VPC peering, create two VPCs with non-overlapping CIDR blocks (10.10.0.0/16 and 10.20.0.0/16), establish a peering connection and configure the route tables to allow resources in both networks to communicate privately.  

## Skill 
* Network architecture and security.
* Virtual private cloud. 


This project highlights my proficiency in advanced AWS networking concepts. Design a Secure Network Topology. Implement a Core Networking Service. I show a clear understanding of how route tables control traffic flow, a critical component of any network. Adhere to Best Practices: Using non-overlapping CIDR blocks is a fundamental requirement for VPC peering, a detail that demonstrates technical accuracy.

## Configuration Details
1. VPC-A: CIDR Block: 10.10.0.0/16

2. VPC-B: CIDR Block: 10.20.0.0/16

3. Subnets: Both VPCs are configured with private and public subnets.

4. VPC Peering Connection: A peering connection is established between VPC-A and VPC-B.

5. Route Tables: The route tables for both VPCs are updated to include a route to the peer VPC via the peering connection.

## Ready for action?

Step 1: Create VPCs and subnets

In the AWS Management Console, navigate to the VPC service.

* Create VPC-A with the CIDR block 10.10.0.0/16.

* Create VPC-B with the CIDR block 10.20.0.0/16.

For each VPC, create a public and a private subnet using CIDR of your choice.

Step 2: Create an Internet Gateway
This internet gateway will be attached to the public subnet of each VPC. This is what gives our VPC access to the internet.

Step 3: Configure Route table
Add each internet gateway to their respective route tables.

Step 4: Create VPC Peering Connection

> Navigate to "Peering Connections" and click "Create peering connection."

> Select VPC-A as the "Requester VPC" and VPC-B as the "Accepter VPC."

> The peering request will be created. You must then navigate to the VPC-B console and "Accept" the peering request.

Step 5: Update Route Tables

* For VPC-A: Navigate to the main route table for VPC-A.

> Edit its routes and add a new route:

> Destination: 10.20.0.0/16 (VPC-B's CIDR)

> Target: Select the VPC peering connection you just created.

* For VPC-B: Navigate to the main route table for VPC-B.

> Edit its routes and add a new route:

> Destination: 10.10.0.0/16 (VPC-A's CIDR)

> Target: Select the VPC peering connection.

[View Demo](#)

Now you have a private, secure network link between two separate virtual networks. You can now launch instances in either VPC and test communication between them. See you later.






