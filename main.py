import praw, yaml, time, traceback

print('Starting up.')

with open("config.yaml") as config_file:
    config = yaml.safe_load(config_file)
    client_id = config["client_id"]
    client_secret = config["client_secret"]
    username = config["username"]
    password = config["password"]
    user_agent = config["user_agent"]
    subs = config["nsfw_subs"]
    removal_message = config["removal_message"]
    
print('YAML loaded.')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=password)

print('Authenticated.')

while True:
    try:
        for submission in reddit.subreddit("lesub").stream.submissions(skip_existing=True):
            print('New submission!')
            is_nsfw = False
            author = submission.author.name
            print('author:',author)
            for submission_2 in reddit.redditor(author).submissions.new(limit=None):
                if submission_2.subreddit.display_name in subs:
                    is_nsfw = not is_nsfw
                    print('nsfw post!')
                    break
            for comment in reddit.redditor(author).comments.new(limit=None):
                if comment.subreddit.display_name in subs:
                    is_nsfw = not is_nsfw
                    print('nsfw comment!')
                    break
            print('IS NSFW???',is_nsfw)
            if is_nsfw == True:
                print('removed submission')
                submission.mod.remove()
                submission.reply(removal_message.format(author))
            else:
                print('No bad posts found.')
    except Exception:
        print(traceback.format_exc())
        time.sleep(60)
