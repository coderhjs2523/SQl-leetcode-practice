SELECT T.tweet_id
FROM Tweets T
WHERE LENGTH(T.content) > 15;