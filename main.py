import praw
import prawcore.exceptions
import re
import lyricsgenius as genius
import requests

def main():
    Bot = create_reddit_bot()
    while True:
        songname,mention = search_for_mention(Bot)
        song_lyrics = find_song(songname)
        if song_lyrics == None:
            mention.reply("Couldnt't find that song")
        else:
            mention.reply(song_lyrics)


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
                if isinstance(mention,praw.models.Comment):
                    if mention.new == True:
                        print("Found one")
                        already_replied_to_comment.add(mention)
                        mention.mark_read()
                        try:
                            songname = re.sub(r"u/SongLad", "", mention.body, flags=re.IGNORECASE)
                            print(songname)
                            songname = songname.strip()
                            return songname, mention
                        except ValueError:
                            mention.reply("no song title was given")

        except prawcore.exceptions.BadRequest:
            print("error")
def find_song(songname):
    Genius = genius.Genius("zH_HyGzT82X43jyLRuf4q2NX1rRp63rPy2sNU4wXNf5nlcmHTgrjhzPwVS19UkQw")
    try:
        song = Genius.search_song(songname)
        if song != None:
            return song.lyrics
    except requests.exceptions.Timeout:
        return None
def format_song_lyrics(song_lyrics):
    song_lyrics = re.sub(r"^.+Lyrics","",song_lyrics)
    formatted_song_lyrics = re.sub(r"\d+Embed$","",song_lyrics)
    return formatted_song_lyrics

if __name__ == "__main__":
    main()
