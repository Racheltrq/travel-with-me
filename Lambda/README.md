Information about Lambda functions:

0. user-cognito: Control users' signin/signup behaviors.
1. search-hotel: Search for hotel with the info given by user.
2. push-hotel-desc: Look up hotel descriptions on website, then push result to DynamoDB.
3. get-hotel-desc: Get hotel descriptions from DynamoDB, prepare to do ML recommendation.
4. hotel-rec: Recommend hotels using ML based on their descriptions after searching.
5. book-hotel: Select a hotel, give more detailed info, book it, prepare to do ML mbti pred.
6. mbti-pred: ML mbti pred.
7. mbti-match: Find a user in DynamoDB that has a matching MBTI type with current user.
8. confirm-partner: Select a partner, send an email to him/her.
