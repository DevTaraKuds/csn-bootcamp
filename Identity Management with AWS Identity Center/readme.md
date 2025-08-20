# Assigning Permissions with AWS Identity Center

In the digital technology space, a fundamental security challenge is managing who has access to what. Granting users excessive permissions can lead to significant security risks, from accidental data deletion to malicious activity. Adhering to the principle of least privilege is essential, but manually configuring fine-grained permissions for every user can be complex and time-consuming. 

## What we can do
I always refer to the framework People, Process and Technology. Where my take is that the people are the weakest link at securing an organizations infrastructure. A comprehensive guide on how to configure user identity and permissions using AWS Identity Center will be provided. It demonstrates a practical application of the least privilege principle by assigning a specific, pre-defined permission set to a user. In this case, the SecurityAudit permission. 

## Result
This will ensures that the user has only the permissions necessary to perform security audits and nothing more, effectively minimizing the organization's risk and exposure to cyber infiltration.

## Why This
This project highlights my expertise in a critical area of cloud security: Identity and Access Management (IAM). It demonstrates my ability to implement security best practices and understand the importance of secure identity configurations. By showing how to use a service like AWS Identity Center, it proves that I am proficient in managing user access at scale, a key skill for any security-focused cloud professional.

## Skills Gained
* Principle of least priviledge.
* Identity and Access Management

## Pre-requisite
1. An active AWS account.
2. Access to AWS Identity Center and the identity center must be enabled.

## Let's get to work

Step 1 : Navigate to the AWS Management Console.
Search for "AWS Identity Center,". If you have never used this before, you will need to enable it by simply clicking "Enable."

Step 2: Create a New User
In the AWS Identity Center dashboard, go to the "Users" section and create a new user if you have not already done this.

Step 3: Create a Permission Set
Under the "Permission sets" section on the left nav pane, select permission set, create a new permission set. For this project, select the "SecurityAudit" policy from the list of pre-defined AWS managed policies.

Step 4: Assign the User to an Account
Go to the "AWS accounts" section, select the account you want to grant access to, and assign the user you created to that account.

Step 5: Assign the Permission Set. 
When assigning the user, select the "SecurityAudit" permission set you have just created.

For a more visual run through of how this can be done, Check my [Youtube Channel Here.](#)

Viola, now you have a user who can log in via AWS Identity Center and has read-only access to audit security configurations, without the ability to make any changes. this is same process for all other permission sets. Feel free to explore.
