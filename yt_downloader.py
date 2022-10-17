# Script for dowloading videos from Youtube using pafy and youtube-dl==2020.12.2

import pafy
import sys

def get_video():
    try:
        url = input("Please enter your video URL: ")
        print("Obtaining video information, please wait...")
        clip = pafy.new(url)
        print(f"Title: {clip.title} | Length: {clip.length} | Rating: {clip.rating}")
        dl = clip.getbest(preftype="mp4")
        print(f"We are downloading at this quality: {dl.resolution} in {dl.extension} format.")
        myfilename = f"{sys.path[0]}/{clip.title}.{dl.extension}"
        print(f"Saving this file as: {clip.title} in {sys.path[0]}/")
        dl.download(progress=False, filepath=myfilename)
    except Exception as err:
        print(f"Oh! You have an error: {err}")
    else:
        print(f"{clip.title} was succesfully downloaded.")
        

get_video()