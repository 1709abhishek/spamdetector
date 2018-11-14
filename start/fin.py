import praw

reddit = praw.Reddit(
client_id = 'Eb9FIjUfJ8zg8A',
client_secret = 'vtwS7Vw-i1w_vpgixFoJXG2w5do',
password = 'qwerty1234',
user_agent = 'achint',
username = 'achint43'
)



subreddit = reddit.subreddit('python')

hot_python = subreddit.hot(limit=3)
for submission in hot_python:
    if not submission.stickied:
        print('Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(submission.title,
                                                                           submission.ups,
                                                                           submission.downs,
                                                                           submission.visited))
subreddit.subscribe()

