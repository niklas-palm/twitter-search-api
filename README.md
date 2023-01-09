# twitter-search-api

Cloudformation template that sets up a Lambda function that uses Twitter's search API. Twitter search query passed to the Lambda function environment as variable.

### Set up credentials

Once you have your consumer key and consumer secret, use the AWS CLI to store them AWS Secrets Manager.

**Consumer key:**

```bash
aws secretsmanager create-secret --name twitter-consumer-key --secret-string 'CONSUMER_KEY_GOES_HERE'
```

**Consumer secret:**

```bash
secretsmanager create-secret --name twitter-consumer-secret --secret-string 'CONSUMER_SECRET_GOES_HERE'
```

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
