from bs4 import BeautifulSoup
import requests
import re

BASE_URL = "http://www.lyrics.com"

lyrics = {}

def get_song_lyrics(artist):
    """
    Compiles a dictionary of all the titles and lyrics of an artist and then writes
    it to a file called lyrics.txt
    """
    artist_url = BASE_URL + "/" + artist
    request = requests.get(artist_url)
    soup = BeautifulSoup(request.content, "lxml")
    gdata = soup.find_all('div',{'class':'row'})

    for item in gdata:
        title = item.find_all('a',{'itemprop':'name'})[0].text
        lyricsdotcom = 'http://www.lyrics.com'
        for link in item('a'):
            try:
                lyriclink = lyricsdotcom+link.get('href')
                req = requests.get(lyriclink)
                lyricsoup = BeautifulSoup(req.content, "lxml")
                lyricdata = lyricsoup.find_all('div', {'id':re.compile('lyric_space|lyrics')})[0].text
                lyrics[title] = lyricdata
            except:
                pass

    file = open("lyrics.txt", "a", encoding='utf8')
    for title in lyrics:
        if "Submit Lyrics" not in lyrics[title]:
            lyrics[title] = lyrics[title].split("---")[0]
            file.write(lyrics[title])
    file.close()


file = open("lyrics.txt", "w")
file.close()

artists = ["Drake", "Eminem", "KendrickLamar", "Jcole", "KanyeWest", "WuTangClan"]
for artist in artists:
    print(artist)
    get_song_lyrics(artist)
