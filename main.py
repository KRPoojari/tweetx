import json

testWords = open("racial.txt", "r") #Reading and storing Sample Words
words = testWords.read().splitlines() 
testWords.close()


testTweets = open("tweets.json", "r") #Reading and storing Sample Tweets
tweets = json.load(testTweets)
testTweets.close()


Tweets = []

for j in tweets['sampleTweets']:
    profaneWordCount = (sum(j.lower().count(i) for i in words))
    Tweets.append([j, profaneWordCount])

for i in Tweets:
    print(i[0], (i[1]) / len(i[0]))