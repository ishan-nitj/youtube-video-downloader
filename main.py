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

title_name=str(raw_input())
data=geturl(title_name)
if data["found"]==False:
	print "Sorry requested title was not found"
else:
	print "Downloading best quality video for "+data["title"]+"....."
	string ="youtube-dl -f bestvideo+bestaudio "+data["link"]
	subprocess.call(string,shell=True)
