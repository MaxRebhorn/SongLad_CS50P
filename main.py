import praw
import prawcore.exceptions


def main():
    global reddit_api_counter
    reddit_api_counter = 0
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
    subreddit = Bot.subreddit("Botsplayhere")
    try:
        comments = 0
        for comment in subreddit.stream.comments():
            comments += 1
            print(comments)
            if "u/SongLad" in comment.body.lower():
                print("Found one")
                comment.reply("Hello i am bot")

    except prawcore.exceptions.BadRequest:
        print("error")


#test if git works lel aaaah waaaaaaaa

if __name__ == "__main__":
    main()
