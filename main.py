from bs4 import BeautifulSoup
import requests
import subprocess

def geturl(videotitle):
	r=requests.get("https://www.youtube.com/results?search_query="+videotitle)
	data=r.text
	soup=BeautifulSoup(data)
	data={}
	try:
		links=soup.find_all("a",class_="yt-uix-sessionlink yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2       spf-link ")
		first_link=links[0]
		title=first_link.string
		link=first_link['href']
		link="https://www.youtube.com"+link
		data["found"]=True
		data["link"]=link
		data["title"]=title
	except:
		data["found"]=False
	return data

song_names=str(raw_input("Enter song titles separated with comma \n"))
list_of_songs=song_names.split(",")
choice=int(raw_input("Do you wish to download audio or video \n 1)Audio \n 2)Video \n"))

if choice==1:
	substring="youtube-dl -f bestaudio "
else:
	substring="youtube-dl -f bestvideo+bestaudio "

for song in list_of_songs:
	data=geturl(song)
	if data["found"]==False:
		print "Sorry the song %s was not found" %(song)
	else:
		print "Downloading "+data["title"]+"....."
		string =substring+data["link"]
		try:		
			subprocess.call(string,shell=True)
			print "Downloaded "+data["title"]
		except Exception as e:
			print "Sorry cant download this song"
			print type(e).__name__		
		print "\n\n"
