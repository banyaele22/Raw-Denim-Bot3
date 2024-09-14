import praw
import config




def bot_login():
    r = praw.Reddit(username = config.username,
        password = config.password,
        client_secret = config.client_secret,
        client_id = config.client_id,
        user_agent = "raw denim agenda bot v0.1"
         )
   
    return r

def run_bot(r):
    for comment in r.subreddit('rawdenim').comments(limit=25):
        if "oni" in comment.body:
            print("test")
            comment.reply("BEST ONI DENIM FADES PHOTO ALBUM!: https://imgur.com/a/6gobsXV ")

r=bot_login()
run_bot(r)


 