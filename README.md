# turbo-mod

Removes both submissions and comments from your moderated subreddit if the user's account has publically interacted (commented/posted) in your list of NSFW subreddits (added in the `config.yaml` file).

As a few examples, the config.yaml file has a small list of NSFW subreddit names already added. You may edit and remove them, and change any variable names in the main.py file as you please.

This code is the bare basics as described above, you can add more moderation features by editing the python code in main.py to fit your needs; you'll likely need to reference [PRAW](https://praw.readthedocs.io/en/stable/code_overview/praw_models.html) documention and view [r/redditdev](https://www.reddit.com/r/redditdev/) to learn more on your own.

# Setup

Clone the github repository, change directories:

    git clone https://github.com/CaringCactus/turbo-mod
    cd turbo-mod

Install the requirements:

    pip3 install -r requirements.txt

Edit the `config.yaml` file with your bot credientials (Never give this information out to anyone, keep your client_secret a secret):

- `client_secret` is your reddit client secret.
- `user_agent` is your unique user agent.
- `client_id` is your client id.
- `username` is your username.
- `password` is your password.
- `mod_sub` is the subreddit you want the bot to operate in.
- `nsfw_subs` is the subreddit(s) you don't like.
- `removal_message` is the comment that the bot will make after removing the submission.

Run the `main.py` file:

    python3 main.py
   
# Prerequisites for hosting your bot's code
If you want to try out the bot locally on your computer, you only need to install PRAW, but it's more convenient to host the code online through cloud services. All needed modules are described in the requirements.txt file.

## Deployment

### First steps
First you would probably want to create a new Reddit account for your bot.

- Go to [Reddit](https://www.reddit.com) and create an account.
- Login and go to [Preferences > Apps](https://www.reddit.com/prefs/apps) and click "create another app...".
- Type a name for your app and choose "script". Add a description and provide the "about" and "redirect" URIs.

### Pre-deployment
- Clone the current repository to your local storage.
- Rename the folder name to anything you need.
- Open the config.yaml and add your Reddit user and app info.
- Make changes to any wording as you please, both in config.yaml or main.py to suit your needs.

### Deployment
- To locally run your bot: Open Bash or CMD and cd to your project folder, then run the program.
- To run your bot in the cloud, follow the instructions from the cloud service provider you are using.

### Post-deployment
- If running locally on your computer, you will have to leave your computer on with the powershell running. For long-term use, you should think about subscribing to a cloud service, or creating your own private server at home with a dedicated device.
- If using a cloud service, verify online the app has been turned and setup propely.
