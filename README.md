
# tweetx

**tweetx** is a program to detect racial slurs in Twitter Tweets.

Racial Abuse on Twitter is becoming quite a serious issue in recent times.\
tweetx aims to flag such tweets by stating a *Degree of Profanity* for each tweet.\
Higher degree of profanity indicates more profanity in the Tweet.

## Uses

Tweets are included in the `tweets.json` file. `racial.txt` consists of words that may indicate racial abuse/slurs. 
These words when found in the Tweets indicate a High Degree of Profanity. 

## Evaluation

Tweets are scanned for words indicating racial slurs. The more number of words detected, the more would be the resulting Degree of Profanity.

![Degree of Profanity](https://latex.codecogs.com/svg.latex?%5Cbg_white%20Degree%20%5C%20of%20%5C%20Profanity%20%3D%20%5Cfrac%7BNumber%20%5C%20of%20%5C%20Profane%20%5C%20Words%5C%20%28Racial%20%5C%20Slurs%29%7D%7BTotal%20%5C%20Number%20%5C%20of%20%5C%20Words%20%5C%20in%20%5C%20the%20%5C%20Tweet%7D)

#### Dependencies

Python3



## License

Copyright (c) **Kartik Poojari**. All rights reserved. Licensed under the MIT License


[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)