# Hosting a Static Website on Amazon S3

Setting up a web server, managing infrastructure, and dealing with maintenance can be time-consuming. This is an highly scalable way to host a static website using Amazon S3, a service designed for object storage.

## Prerequisite

1.	A static website consisting of an index.html file and a few assets (CSS, images).
2.	Use a public S3 bucket to store the HTML, CSS, and image files for the website.
3. Configure the bucket to allow public access for website viewing.
4. Enable S3's built-in static website hosting feature to serve the content.
5. Create a policy that allows for specific action ensuring least privilege access.


##Skills Displayed

⦁	Website Administration and deployment
⦁	Scalability
⦁	Load balancing 
⦁	Security Best Practices via policies.


## Ready or Not?
Step 1: Create an S3 Bucket
⦁	In the AWS console, navigate to the S3 service.

⦁	Click "Create bucket." Give it a unique name.

⦁	Uncheck "Block all public access." 
⦁	Create Bucket

Step 2: Enable Static Website Hosting
⦁	Go to the "Properties" tab of your new bucket.
⦁	Scroll down to "Static website hosting" and click "Edit."
⦁	Select "Enable" and enter index.html as the index document. Save changes.

Step 3: Upload Your Files
⦁	Go to the "Objects" tab and upload your index.html file and any other assets (CSS, images).

Step 4: Set a Bucket Policy
⦁	Go to the "Permissions" tab and click "Edit" on the "Bucket policy" section. click here to view the [bucket policy JSON file](#)
⦁	Add a policy that allows public read access. The policy should look like this (remember to replace your-bucket-name):

Step 5: Access Your Website
⦁	Go back to the "Properties" tab, and under "Static website hosting," you'll find the bucket's public URL.
⦁	Preview your fully hosted website.

View [Video Demo here.](#)

There you go! You to the world. Happy? Yeah sure you are. 
