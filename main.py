import praw
def main():
    Bot = create_reddit_bot()
    search_for_mention(Bot)


def create_reddit_bot():
    client_id = "O3RiRmUYrNRBi85XK5KDtw"
    client_secret = "8GldRw4lvXHBxq4Fo4PPeaeZiV1IGA"
    username = "songlad"
    password = "mybot1salad"
    user_agent = "windows:SongLad:1.0"
    Bot = praw.Reddit(client_id=client_id,client_secret=client_secret,username=username,password=password,user_agent=user_agent)
    return Bot

def search_for_mention(Bot):
    Bot.subreddit


#test if git works

if __name__ == "__main__":
    main()
