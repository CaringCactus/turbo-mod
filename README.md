# turbo-mod

removes submissions from users who participate in subreddits you don't like.

# setup

Clone the repo, change directories:

    git clone https://github.com/IThinkImOKAY/turbo-mod
    cd turbo-mod

Install the requirements:

    pip3 install -r requirements.txt

Edit the `config.yaml` file:

- `client_secret` is your reddit client secret
- `user_agent` is your unique user agent
- `client_id` is your client id
- `username` is your username
- `password` is your password
- `mod_sub` is the subreddit you want the bot to operate in
- `nsfw_subs` is the subreddits you don't like
- `removal_message` is the comment that the bot will make after removing the submission

Run the `main.py` file:

    python3 main.py
