import praw

reddit = praw.Reddit(
client_id = 'Eb9FIjUfJ8zg8A',
client_secret = 'vtwS7Vw-i1w_vpgixFoJXG2w5do',
password = 'qwerty1234',
user_agent = 'achint',
username = 'achint43'
)

subreddit = reddit.subreddit('news')

conversedict = {}
hot_python = subreddit.hot(limit=3)

for submission in hot_python:
    if not submission.stickied:
        print('Title: {}, ups: {}, downs: {}, Have we visited?: {}, subid: {}'.format(submission.title,
                                                                                                   submission.ups,
                                                                                                   submission.downs,
                                                                                                   submission.visited,
                                                                                                   submission.id))

        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            if comment.id not in conversedict:
                conversedict[comment.id] = [comment.body,{}]
                if comment.parent() != submission.id:
                    parent = str(comment.parent())
                    conversedict[parent][1][comment.id] = [comment.ups, comment.body]


# Dictionary Format#
'''
conversedict = {post_id: [parent_content, {reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content]}],

                post_id: [parent_content, {reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content]}],
                                            
                post_id: [parent_content, {reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content]}],
                }


'''

for post_id in conversedict:
    message = conversedict[post_id][0]
    replies = conversedict[post_id][1]
    if len(replies) > 1:
        print('Original Message: {}'.format(message))
        print(35*'_')
        print('Replies:')
        for reply in replies:
            print(replies[reply])

