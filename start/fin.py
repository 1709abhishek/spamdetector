import praw
import sys, os

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

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
    
    # No: operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
if not foo is None:
    spam( ham[ 1 ], { eggs: 2 } )
    def foo(x):
    if x >= 0:
        return math.sqrt(x)

    def bar(x):
        if x < 0:
            return
         return math.sqrt(x)
    f = lambda x: 2*x
    
    
try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None
