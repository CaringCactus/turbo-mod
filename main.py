import praw, yaml, time, traceback

with open("config.yaml") as config_file:
    config = yaml.safe_load(config_file)
    client_id = config["client_id"]
    client_secret = config["client_secret"]
    username = config["username"]
    password = config["password"]
    user_agent = config["user_agent"]
    mod_sub = config["mod_sub"]
    subs = config["nsfw_subs"]
    removal_message = config["removal_message"]

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=password)

streamSubmissions = reddit.subreddit(mod_sub).stream.submissions(pause_after=-1, skip_existing=True)
streamComments = reddit.subreddit(mod_sub).stream.comments(pause_after=-1, skip_existing=True)


print('About to start while loop!')
while True:
    try:
        for submission in streamSubmissions:
            if submission is None:
                break
            else:
                is_nsfw = False
                author = submission.author.name
                
                userSubmissions = reddit.redditor(author).submissions.new(limit=None)
                for acct_submission in userSubmissions:
                    if acct_submission.subreddit.display_name in subs:
                        is_nsfw = True
                        break
                userComments = reddit.redditor(author).comments.new(limit=None)
                for acct_comment in userComments:
                    if acct_comment.subreddit.display_name in subs:
                        is_nsfw = True
                        break
                if is_nsfw == True:
                    print('New submission from u/' + author + ': Removed due to NSFW account activity found.')
                    submission.mod.lock()
                    submission.mod.remove()
                    submission.reply(removal_message.format(author))
                    break
                else:
                    print('New submission from u/' + author + ': Clean account.')
                    break
                    
        for comment in streamComments:
            if comment is None:
                break
            else:
                is_nsfw = False
                author = comment.author.name
                
                userSubmissions = reddit.redditor(author).submissions.new(limit=None)
                for acct_submission in userSubmissions:
                    if acct_submission.subreddit.display_name in subs:
                        is_nsfw = True
                        break
                userComments = reddit.redditor(author).comments.new(limit=None)
                for acct_comment in userComments:
                    if acct_comment.subreddit.display_name in subs:
                        is_nsfw = True
                        break
                if is_nsfw == True:
                    print('New comment from u/' + author + ': Removed due to NSFW account activity found.')
                    comment.mod.remove()
                    comment.reply(removal_message.format(author))
                    break
                else:
                    print('New comment from u/' + author + ': Clean account.')
                    break
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
