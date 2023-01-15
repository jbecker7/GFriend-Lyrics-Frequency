import lyricsgenius as genius

# initialize Genius API object
genius_api = genius.Genius("key here")

# search for GFriend songs
gfriend_songs = genius_api.search_artist("GFriend", max_songs=50)

# get the lyrics of all the songs
lyrics = ""
for song in gfriend_songs.songs:
    lyrics +=song.lyrics + " "

# split lyrics into words
words = lyrics.split()

# list of words to exclude
exclude_words = ["Yuju,", "Eunha,", "Yerin,", "SinB,", "Sowon,", "Umji,","[Verse","[Chorus:","Lyrics[여자친구","가사]","Yuju]","Yerin]","SinB]","Umji]" ]

# count the frequency of each word
word_freq = {}
for word in words:
    # check if word is in exclude list
    if word not in exclude_words:
        word_freq[word] = word_freq.get(word, 0) + 1

# find the 30 most common words
most_common = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:30]

# extract the words and frequency counts
words = [word for word, freq in most_common]
freqs = [freq for word, freq in most_common]

# print the most common words
print("The 30 most common words used in GFriend's songs are:")
for word, freq in most_common:
    print(f"{word}: {freq}")