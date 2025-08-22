# Secure Static Website Hosting with AWS Route 53, CloudFront, and ACM

Deploying a website is one thing, but making it fast, secure, and accessible via a custom domain is a different challenge entirely. This project addresses the complexities of orchestrating multiple cloud services to create a professional web presence. It provides a complete guide to connecting a custom domain, securing it with an SSL certificate, and distributing content globally via a Content Delivery Network (CDN). The solution leverages several key AWS services to handle the domain, SSL, and content delivery, resulting in a fast, encrypted, and globally available website.

## Skills
1.	Web Development Lifecycle.
2.	DNS configuration.
3.	CDN deployment.
4.	SSL management.


Domain Name System (DNS): The ability to manage and update domain records using Route 53.

Content Delivery Networks (CDNs): The use of CloudFront to improve site performance and reduce latency for global users.

SSL/TLS Management: The critical process of provisioning and validating SSL certificates with AWS Certificate Manager (ACM) to enable HTTPS.


## Prerequisite

⦁	Domain Registrar: A third-party service used to purchase and manage the custom domain.

⦁	AWS Route 53: Amazon's highly available and scalable DNS web service.

⦁	Amazon S3: Used as the origin for the static website content.

⦁	AWS Certificate Manager (ACM): A service to provision, manage, and deploy SSL/TLS certificates for AWS services.

⦁	Amazon CloudFront: A CDN service that caches content at edge locations worldwide, improving delivery speed and adding a layer of security.

## Getting things started

Step 1: Register a Domain
First, purchase a domain name from a registrar of your choice (e.g., GoDaddy, Namecheap). For practice purposes, you can purchase a free domain. I used dedyn.io. This will be the custom domain for your website.

Step 2: Create an S3 Bucket and Upload Content
⦁	Create an S3 bucket with a name that exactly matches your custom domain (e.g., www.yourdomain.com). At this point, you can opt for blocking public access, your bucket will still be accessible when we edit the policy to allow cloudfront only to access our bucket.

⦁	Upload your static website files (index.html, CSS, etc.) to the bucket.

⦁	In the S3 bucket properties, enable Static website hosting and specify your index and error documents.

⦁	Set a bucket policy to allow public read access (s3:GetObject) and access to cloudfront [view policy here](https://github.com/DevTaraKuds/csn-bootcamp/tree/main/Custom%20Domains%20and%20Certificate%20Management).

Step 4: Request an SSL Certificate with ACM
⦁	In the ACM service, request a public certificate for your custom domain using wildcards (e.g.*.yourdomain.com).

⦁	Choose DNS validation. ACM will provide a CNAME record.

⦁	Go to your Domain portal or Hosted Zone in Route 53 (depending on your case) and create this CNAME record. ACM will automatically validate the certificate once the DNS record propagates.
⦁	Records are updated in Route53 as well

Step 5: Create a CloudFront Distribution
⦁	In the CloudFront service, create a new distribution.

⦁	For the Origin Domain, select your S3 bucket's  (not the S3 bucket website endpoint).

⦁	Under Viewer Protocol Policy, select "Redirect HTTP to HTTPS."

⦁	For Alternate Domain Names (CNAMEs), enter your custom domain (e.g., www.yourdomain.com).

⦁	Under Custom SSL Certificate, select the ACM certificate you just validated.

Step 6: Validate DNS and Confirm HTTPS if you used Domain Services
⦁	Go back to your Domain portal.

⦁	Create a new CNAME Record.

⦁	Set the subname to www, target hostname the cloudfront distribution domain name.

Please note that different domain management portals have different processes.

Step 6: Validate DNS and Confirm HTTPS if you used Route 53

⦁	Go back to your Hosted Zone in Route 53 or Domain portal.

⦁	Create a new Record.

⦁	Set the Record type to A.

⦁	Enable the Alias toggle and select your CloudFront distribution as the target.

Save the record. After a few minutes, open a web browser and navigate to your custom domain using https://. The site should load securely, served directly from CloudFront.

[Full Video demo can be seen here](https://youtu.be/Ay5UMI2-EFE)

Now you can combine the speed of a CDN, the reliability of S3, and the security of a custom SSL certificate. You've got this.
