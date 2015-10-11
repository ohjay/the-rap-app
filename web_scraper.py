from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

# from urllib2 import urlopen

# BASE_URL = "http://www.azlyrics.com"

# def get_song_links(artist_url):
#     html = urlopen(artist_url).read()
#     soup = BeautifulSoup(html, "lxml")
#     songs = soup.find("div", "album")
#     song_links = [BASE_URL + link.get('href') for link in songs.findAll("a")]
#     return song_links

# def get_song_lyrics(song_link):
# 	html = urlopen(artist_url).read()
#     soup = BeautifulSoup(html, "lxml")

BASE_URL = "http://genius.com"
 
def get_song_lyrics(artist):
	"""Returns all the song lyrics of a certain artist.
	"""
	artist_url = BASE_URL + "/artists/ " + artist + "/"
	response = requests.get(artist_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'})

	soup = BeautifulSoup(response.text, "lxml")
	for song_link in soup.select('ul.song_list > li > a'):
	    link = urljoin(BASE_URL, song_link['href'])
	    response = requests.get(link)
	    soup = BeautifulSoup(response.text)
	    lyrics = soup.find('div', class_='lyrics').text.strip()
	return lyrics
