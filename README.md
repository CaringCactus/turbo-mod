# turbo-mod

Removes post submissions from your moderated subreddit if the user has publically interacted (commented or posted) from any subreddit you add to the list in the `config.yaml` file.

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
If you want to try out the bot locally on your computer, you only need to install PRAW, but it's more convenient to host the code online through cloud services such as Heroku. All needed modules are described in the requirements.txt file.

Heroku is an online cloud hosting service for applications (code), it's the best way to run your one (1) bot for free. Unverified accounts get 550 free hours per month (which is not enough to run your bot 24/7), so you will need to verify your heroku account with a credit card to get 1000 free hours per month. You can learn more about verification on their [webstie here](https://www.heroku.com/free).

## Deployment

### First steps
First you would probably want to create a new Reddit account for your bot.

- Go to [Reddit](https://www.reddit.com) and create an account.
- Login and go to Preferences > Apps and click "create another app...".
- Type a name for your app and choose "script". Add a description and provide the "about" and "redirect" URIs.

Next, you will need to create a new heroku account if you don't have one already.

- Go to [Heroku](https://www.heroku.com) and create an account.
- Create a Heroku app.
- Download and install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
- Open Bash or CMD and login to Heroku CLI `$ heroku login`.

### Pre-deployment
- Clone the current repository to your local storage.
- Rename the folder name to anything you need.
- Open the friendbot.py and hintbot.py files and add your Reddit user and app info.
- Make changes to both of these files to suit your needs.

### Deployment
- Open Bash or CMD and cd to your project folder.
- Change your remote to `$ heroku git:remote -a your_heroku_app_name`.
- Add a buildpack to Heroku so it can understand that this is a Python app. `heroku buildpacks:set heroku/python`
- Commit your changes. `git add .`, `git commit -m "make better"`.
- Deploy your app by typing `git push heroku master`.
- You can view what the app is printing at a given time by typing `heroku logs`.

### Post-deployment
- Go to [Heroku](https://www.heroku.com) and go to you app administration.
- Select "Resources" and press the pen button beside your dyno.
- Change the slider to active and press confirm.
- Press "More" on the top right corner and then "View Logs".
- There should be a line `State changed from starting to up`, that means that your app is up and running.
