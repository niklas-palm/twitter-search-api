# twitter-search-api

Cloudformation template that sets up a Lambda function that uses Twitter's search API. The search query passed to the Lambda function environment as variable. By default, the Lambda Function is triggered once every minute.

### Set up credentials

On Twitter's [developer portal](https://developer.twitter.com/en/portal/dashboard), follow the instructions to create a new app and retreive the credentials. Once you have your consumer key and consumer secret, use the AWS CLI to store them AWS Secrets Manager.

**Consumer key:**

```bash
aws secretsmanager create-secret --name twitter-consumer-key --secret-string 'CONSUMER_KEY_GOES_HERE'
```

**Consumer secret:**

```bash
secretsmanager create-secret --name twitter-consumer-secret --secret-string 'CONSUMER_SECRET_GOES_HERE'
```

### Twitter search query

To change the search query, update the environment variable passed to the Lambda Function. To manipulate other parameters, update the Lambda function code. Documentation on how to build the search query can be found [here](https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query).

### Deploy

Using AWS SAM, you can deploy the Lambda function

**First time:**

```bash
sam build && sam deploy --guided
```

**!First time:**

```bash
sam build && sam deploy
```
