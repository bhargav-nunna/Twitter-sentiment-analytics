# Twitter-sentiment-analytics
Sentiment Analysis on Twitter

getBacthData -> Fetches tweets with specified hashtag and dumps them to 'tweetDump.json'
preProcesTweets -> Extract each tweet from dump and tokenize. Also apply regex to recognize URLs and emoticons.
tweetTermFreaquency -> Find out most commonly used terms. Remove stop words and apply custom filters. 