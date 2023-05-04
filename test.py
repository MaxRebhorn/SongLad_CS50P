from main import format_song_lyrics
def main():
    test_format_song_lyrics()
def test_format_song_lyrics():
    song_lyrics_input = str(open("song_lyrics","r"))
    song_lyrics = str(open("song_lyrics_correct","r"))
    song_lyrics = format_song_lyrics(song_lyrics)
    assert "Contributers" not in song_lyrics
























if __name__ == "main":
    main()



