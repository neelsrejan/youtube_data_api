import os
import time
import shutil
from math import ceil
from datetime import date, timedelta
from YT_CHANNEL import YT_CHANNEL
from clean_data import clean_data

def main():
    
    # Ask user for authentication and what YouTube channel they want information about
    print("Welcome to the YouTube Data API page!")
    API_KEY = input("What is your YouTube data API KEY? ")
    channel_id = input("What is the ID of the YouTube channel you with to get information about? ")

    # Get channel metadata of channel name, number of videos, video ids, and playlist ids
    print("Getting metadata")
    YT = YT_CHANNEL(API_KEY, channel_id, str(date.today()))
    if YT.API_COST + 6 < 10000:
        YT.get_channel_metadata()

    # Create directories for saving data into when running functions
    if not os.path.exists(os.path.join(os.getcwd(), f"{YT.channel_name}_data", f"{YT.date}")):
        data_categories = ["activity", "channels", "channel_sections", "comments", "playlists", "playlist_items", "search", "videos"]
        for data_category in data_categories:
            os.makedirs(os.path.join(os.getcwd(), f"{YT.channel_name}_data", f"{YT.date}", "raw", f"{data_category}"))
            os.makedirs(os.path.join(os.getcwd(), f"{YT.channel_name}_data", f"{YT.date}", "clean", "csv", f"{data_category}"))
            os.makedirs(os.path.join(os.getcwd(), f"{YT.channel_name}_data", f"{YT.date}", "clean", "xlsx", f"{data_category}"))

    #Check to see if there is month old data as YT_data_api requires all data from a month or older be deleted
    if os.path.exists(os.path.join(os.getcwd(), f"{YT.channel_name}_data")):
        today = date.today()
        month_ago = today - timedelta(days=30)

        to_rem = []
        directories = os.listdir(os.path.join(os.getcwd(), f"{YT.channel_name}_data"))
        for directory in directories:
            year, month, day = [int(i) for i in directory.split("-")]
            date_dir = date(year, month, day)
            if month_ago > date_dir:
                to_rem.append(directory)

        if len(to_rem) > 0:
            for too_old in to_rem:
                shutil.rmtree(os.path.join(os.getcwd(), f"{YT.channel_name}_data", too_old))
    
    # Get all data
    print("Getting data")
    if YT.API_COST + 16 < 10000:
        YT.get_activity()
        YT.get_channels()
        YT.get_channel_sections()
        YT.get_playlists()
        YT.get_playlist_items()
    
    not_done = True
    vid_ids = YT.vid_ids
    while not_done:
        while len(vid_ids) != 0:
            vid_id = vid_ids.pop(0)
            num_comments = YT.get_num_comments(vid_id)
            vid_cost = ceil(int(num_comments)/100) + 103

            if YT.API_COST + vid_cost < 10000:
                YT.get_video(vid_id)

                vid = YT.make_comment(API_KEY, vid_id, YT.channel_name, YT.date)
                vid.comment_ids = vid.get_vid_comment_ids()
                vid.get_vid_comments()
                YT.API_COST += vid.COMMENT_API_COST

                YT.get_search(vid_id)
            else:
                time.sleep(60*60*24)
                YT.API_COST = 0
                print("API Cost is about to cross 10,000, program will run for another day and continue when new API credits are there to be used.")
                print("The current API Credits used today is: ", YT.API_COST)
                break
        if len(vid_ids) == 0:
            not_done = False
      
    # Clean data into excel/csv
    print("Cleaning data")
    clean_data(YT.channel_name, YT.vid_ids, YT.playlist_ids, YT.date)
    print("Complete, your data has been gathered and cleaned!")
    print("The current API Credits used today is: ", YT.API_COST)

if __name__ == "__main__":
    main()
