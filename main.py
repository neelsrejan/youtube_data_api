import os
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

    # Create directories for saving data into when running functions
    if not os.path.exists(os.path.join(os.getcwd(), f"{YT.channel_name}_data", f"{date.today()}")):
        data_categories = ["activity", "captions", "channels", "channel_sections", "comments", "playlists", "playlist_items", "search", "videos"]
        for data_category in data_categories:
            os.makedirs(os.path.join(os.getcwd(), f"{YT.channel_name}_data", f"{date.today()}", f"{data_category}"))

    # Get all data
    YT.get_activities(2 * YT.num_vids)
    YT.get_captions()
    YT.get_channels()
    YT.get_channel_sections()
    for vid_id in YT.vid_ids:
        vid = YT.make_Comment(API_KEY, vid_id, YT.channel_name)
        vid.comment_ids = vid.get_vid_comment_ids()
        vid.get_vid_comments()
    YT.get_playlists()
    YT.get_playlist_items(2 * YT.num_vids)
    YT.get_related_vids()
    YT.get_video()

if __name__ == "__main__":
    main()
