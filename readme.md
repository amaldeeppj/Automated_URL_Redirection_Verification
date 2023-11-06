# Automated URL Redirection Verification Tool

## Problem Statement

In assisting SEO teams, we must implement a multitude of redirection rules on the servers. While adding redirection rules in bulk can be achieved using text manipulation techniques, ensuring the accuracy of these redirections is equally crucial. Manually verifying a handful of URLs is manageable, but when dealing with thousands of them, the task becomes impractical. Moreover, it's essential to validate the functioning of various URL combinations, including http://, https://, http://www, and https://www.

## Solution

To address this challenge, I proposed the development of a script capable of systematically validating redirections. The script will take each URL and combine it with the aforementioned URL variations (http://, https://, http://www, and https://www). Subsequently, it will send requests to these URLs and check if they redirect correctly.

## Implementation

### Prerequisites

Before implementing the solution, it's important to understand the prerequisites:

1. **Create a List of URLs**: We need a list of URLs to work with. Python's text manipulation capabilities will be utilized to generate this list.

2. **Retrieve Redirected Paths**: The tool will use the curl command to follow redirections. While Python can be used to run curl, it may experience timeout issues with a large number of URLs. For better performance, the Linux command for curl is used. This can be accessed from Python or, for optimal performance, executed using a Bash script.

### Implementation Steps

To implement the solution, followed these steps:

1. **Generate the URL List**: Utilize Python's text manipulation capabilities to create a list of URLs. This list should include the URLs you want to validate.

2. **Execute Bash Program**: Send the generated URL list to a Bash program. The Bash program will read the list and use the curl command to visit each URL. It will record the HTTP response code and the redirected URL. These results will be stored in a CSV file, along with the desired redirection URL.

3. **Verify Redirection**: The Bash program will also verify if the redirected URL matches the expected output.

## Post-Implementation Usage

Once the tool has been executed, you will have a CSV file containing data about the redirections and their accuracy. This CSV file can be utilized for data visualization and further analysis.

By following these steps, you can automate the verification of a large number of redirection rules, making SEO management more efficient and reliable.