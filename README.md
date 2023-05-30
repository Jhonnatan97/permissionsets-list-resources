# AWS SSO Policy Permissions Checker

Here's a Python script that lets you check if a certain type of permission is present in policies associated with AWS SSO permission sets.

## Prerequisites

Before running this script, make sure you have the following dependencies installed:

- Python 3.x
- boto3 library

Additionally, you will need to configure your AWS access credentials for authentication. See the [boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration) for more information on configuring your credentials.

## Settings

1. Download or clone this repository to your local machine.

2. Open the `script.py` file in a text editor.

3. Replace `<your-profile>` with the profile name from your AWS credentials.

4. Replace `<your-instance>` with the ARN of the AWS SSO instance you want to check policies for.

5. Specify the desired permission type in the `permission_type` variable. For example, if you want to check for the presence of the "cloudtrail" permission, set `permission_type = "cloudtrail"`.

6. Save changes to the file.

## Running the script

In the terminal, navigate to the directory where you saved the `script.py` file and run the following command:

```
python script.py
```

This will run the script and print information about the permission sets and their associated policies to the output.

## Sample Output

The output of the script will look like the following:

```
Name PermissionSet: ExamplePermissionSet - Police AWS: ExamplePolicy Arn: arn:aws:iam::<your-account>:policy/ExamplePolicy
{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": [
"cloudtrail:DescribeTrails",
"cloudtrail:GetTrailStatus"
],
"Resource": "*"
}
]
}
```
The cloudtrail permission is present in the inline policy.
  
This indicates that the "cloudtrail" permission is present in the inline policy of the "ExamplePermissionSet" permission set.
