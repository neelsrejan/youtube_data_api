# Welcome to the Youtube Data API

## Abstract
I have been wanting to figure out a way to scrape data from the Youtube Data Api V3 as my friend has recently created a youtube channel for himself. As I am not the owner of the channel and don't have his login credentials I figured I should make a generic python program that allows anyone to gather information on any youtube channel they wish to pull data on. In this program one simply needs to enter the channel id of the channel they wish to get information from as well as their own personal google console api key. With this, the program will gather information on all videos the channel has. The limitation of the program is due to google console's 10,000 unit cost per day which limits the program's completion. Thus the program can take 1+ days to run based on the amount of main comments on a video and search costing 100 units per video. But once the program eventually finishes, the progam then sorts relevant data into csv/excel files.

## Methodology
To use the code, clone the repo into a folder where you want the data to be stored on your local computer. Make sure you have installed python to run the program by running the command python main.py in the console. Enter your API KEY as well as the youtube channel id you wish to get information on. The program then gets metadata for the channel such as the name, all video/playlist ids, number of videos, and the current date. From there the program makes calls to the activity, channels, channel sections, playlists, playlist items and then video by video through the comments, comment threads, search, and videos endpoints. Once all data gotten back from the api response is saved as a json file, the final step is for the clean data file to extract the json data and put it into a dataframe that is then saved into a .csv and .xlsx file for any system to then analyze.

## Warnings
The program does not store your API KEY. The program does add folders to your local system in which data gathered will be stored. If you wish to use the program, just know that it is up to you to ensure the main.py file is in a location you wish to run it.

## Thank You for checking my project out!
