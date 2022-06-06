from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import PySimpleGUI as sg
import os


sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('enter the name of your YT music are you looking for ? :')],
            [sg.Text(''), sg.InputText()],
            [sg.Button('Download')] ]

# Create the Window
window = sg.Window('GorretSecureFile', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Download': # if user closes window or clicks cancel
        break
    print('Tu as entre ', values[0])

window.close()

music = values[0]
# set the whole YT query
url = "https://www.youtube.com/results?search_query=" + music

# forge an User Agent identity to make YT think that this is a real browser, not a scraper
headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

# string manipulation to process the crap that google sends us in order to generate the url of the video to download.
req = requests.get(url, headers=headers).text
soup = BeautifulSoup(req, "html.parser")
html = soup.prettify('utf-8')
gorret = str(html)
index = gorret.index("/watch?v=") # We assume that this is the first instance of url with "/watch?v="
urlWatch = gorret[index:index+20]
youtube_video_url = "https://www.youtube.com" + urlWatch

print("Video to download:" + youtube_video_url)
print("Please wait...")

#ask for the link from user
link = youtube_video_url
yt = YouTube(link)

#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")
