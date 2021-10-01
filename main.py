import os
import time
from math import ceil
from datetime import date
from YT_CHANNEL import YT_CHANNEL

def main():
    
    # Ask user for authentication and what YouTube channel they want information about
    print("Welcome to the YouTube Data API page!")
    API_KEY = input("What is your YouTube data API KEY? ")
    channel_id = input("What is the ID of the YouTube channel you with to get information about? ")

    # Get channel metadata of channel name, number of videos, video ids, and playlist ids
    YT = YT_CHANNEL(API_KEY, channel_id)
    YT.get_channel_metadata()
    print("Metadata Cost: ", YT.API_COST)

    # Create directories for saving data into when running functions 
    if not os.path.exists(os.path.join(os.getcwd(), f"{YT.channel_name}_data", f"{date.today()}")):
        data_categories = ["activity", "channels", "channel_sections", "comments", "playlists", "playlist_items", "search", "videos"]
        for data_category in data_categories:
            os.makedirs(os.path.join(os.getcwd(), f"{YT.channel_name}_data", f"{date.today()}", f"{data_category}"))

    # Get all data
    if YT.API_COST + 16 < 10000:
        YT.get_activities()
        print("Activities Cost: ", YT.API_COST)
        YT.get_channels()
        print("Channels Cost: ", YT.API_COST)
        YT.get_channel_sections()
        print("Channel Section Cost: ", YT.API_COST)
        YT.get_playlists()
        print("Playlist Cost: ", YT.API_COST)
        YT.get_playlist_items()
        print("Palylist Items: ", YT.API_COST)
    
    print("All cost beside comments, search, videos: ", YT.API_COST)

    not_done = True
    tot_vids = len(YT.vid_ids)
    while not_done:
        while len(YT.vid_ids) != 0:
            vid_id = YT.vid_ids.pop(0)
            num_comments = YT.get_num_comments(vid_id)
            vid_cost = ceil(int(num_comments)/100) + 103

            if YT.API_COST + vid_cost < 10000:
                YT.get_video(vid_id)

                vid = YT.make_comment(API_KEY, vid_id, YT.channel_name)
                vid.comment_ids = vid.get_vid_comment_ids()
                vid.get_vid_comments()
                YT.API_COST += vid.COMMENT_API_COST

                YT.get_related_vids(vid_id)
                print(f"Cost of {vid_id} for comment, serarch, videos: ", YT.API_COST) 
            else:
                time.sleep(60*60*24)
                YT.API_COST = 0
                print("Too much, need another day")
                break
        if len(YT.vid_ids) == 0:
            not_done = False
            print("done")

    # Clean data into excel/csv
    #YT.clean_data()
    print("Total Cost: ", YT.API_COST)

if __name__ == "__main__":
    main()
