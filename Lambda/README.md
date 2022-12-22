## Information about Lambda functions:
0. user-cognito: Control users' signin/signup behaviors.
1. search-hotel: Search for hotel with the info given by user.
2. push-hotel-desc: Look up hotel descriptions on website, then push result to DynamoDB.
3. get-hotel-desc: Get hotel descriptions from DynamoDB, prepare to do ML recommendation.
4. hotel-rec: Recommend hotels using ML based on their descriptions after searching.
5. book-hotel: Select a hotel, give more detailed info, book it, prepare to do ML mbti pred.
6. mbti-pred: ML mbti pred.
7. mbti-match: Find a user in DynamoDB that has a matching MBTI type with current user.
8. confirm-partner: Select a partner, send an email to him/her.


## Deploying Docker Images to Lambda Function:
0. Download Docker [here](https://www.docker.com/), then start Docker.
1. `aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin IAM_NUM.dkr.ecr.us-east-1.amazonaws.com`
2. (OPTIONAL, if repo already created) `aws ecr create-repository --repository-name travelwithme --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE`
3. `cd hotel_rec` / `cd mbti_pred`
4. `docker build -t travelwithme .`
5. `docker tag travelwithme:hotel_rec IAM_NUM.dkr.ecr.us-east-1.amazonaws.com/travelwithme:hotel_rec` / \
`docker tag travelwithme:mbti IAM_NUM.dkr.ecr.us-east-1.amazonaws.com/travelwithme:mbti`
6. `docker push IAM_NUM.dkr.ecr.us-east-1.amazonaws.com/travelwithme:hotel_rec` / \
`docker push 966479700385.dkr.ecr.us-east-1.amazonaws.com/travelwithme:mbti`
