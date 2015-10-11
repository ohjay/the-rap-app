from bs4 import BeautifulSoup
import requests
import re

# http://stackoverflow.com/questions/24873773/web-scraping-rap-lyrics-on-rap-genius-w-python

# from urllib.parse import urljoin
# from urllib2 import urlopen

# BASE_URL = "http://www.azlyrics.com"

# def get_song_links(artist_url):
#     html = urlopen(artist_url).read()
#     soup = BeautifulSoup(html, "lxml")
#     songs = soup.find("div", "album")
#     song_links = [BASE_URL + link.get('href') for link in songs.findAll("a")]
#     return song_links

# def get_song_lyrics(song_link):
#   html = urlopen(artist_url).read()
#     soup = BeautifulSoup(html, "lxml")

# BASE_URL = "http://genius.com"
 
# def get_song_lyrics(artist):
#   """Returns all the song lyrics of a certain artist.
#   """
#   artist_url = BASE_URL + "/artists/ " + artist + "/"
#   response = requests.get(artist_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})

#   soup = BeautifulSoup(response.text, "lxml")
#   for song_link in soup.select('ul.song_list > li > a'):
#       link = urljoin(BASE_URL, song_link['href'])
#       response = requests.get(link)
#       soup = BeautifulSoup(response.text)
#       lyrics = soup.find('div', class_='lyrics').text.strip()
#   return lyrics

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
