from os import environ
from YT_CHANNEL import YT_CHANNEL

def main():
    API_KEY = environ["YOUTUBE_DATA_API_KEY"]
    channel_id = input("Welcome to the Youtube Data API page \nWhat is the ID of the channel you with to get information about? ")
    YT = YT_CHANNEL(API_KEY, channel_id)
    YT.get_channel_metadata()
    YT.get_activities(2*YT.num_vids)
    YT.get_captions()
    YT.get_channels()

if __name__ == "__main__":
    main()
