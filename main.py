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
    already_replied_to_comment = set()
    while True:
        try:
            comments = 0
            for mention in Bot.inbox.mentions():
                comments += 1
                print(comments)
                if isinstance(mention,praw.models.Comment):
                    if mention not in already_replied_to_comment:
                        if mention.submission.is_video:
                            print("Found one")
                            already_replied_to_comment.add(mention)
                            mention.reply("Hello i am bot")

        except prawcore.exceptions.BadRequest:
            print("error")
def find_song():
    ...
#test if git works lel aaaah waaaaaaaa

if __name__ == "__main__":
    main()
