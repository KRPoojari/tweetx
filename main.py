import json

#Reading Data
with open("racial.txt", "r") as testWords, open("tweets.json", "r") as testTweets: 
    words = testWords.read().splitlines() 
    tweets = json.load(testTweets)

Tweets = []

#Detection of Profane words(racial slurs)
for j in tweets['sampleTweets']:
    profaneWordCount = (sum(j.lower().count(i) for i in words))
    Tweets.append([j, profaneWordCount])

#Determining the Degree of Profanity of each tweet
'''Degree was determined on the basis of ratio of Profane Words 
to the Total Number of Words in the tweet.'''
for i in Tweets:
    rawScore = (i[1]) / len(i[0])
    if rawScore == 0.0:
        degree = "NOT PROFANE"
    elif rawScore > 0.0 and rawScore < 0.025:
        degree = "PROFANE"
    elif rawScore > 0.025 and rawScore < 0.05:
        degree = "VERY PROFANE"
    else:
        degree = "EXTREMELY PROFANE"        
    print(i[0], "-" , degree, "(", rawScore, ")", "\n")