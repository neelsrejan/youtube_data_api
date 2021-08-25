from os import environ
from YT_CHANNEL import YT_CHANNEL

def main():
    API_KEY = environ["YOUTUBE_DATA_API_KEY"]
    channel_id = input("Welcome to the Youtube Data API page \nWhat is the ID of the channel you with to get information about? ")
    YT = YT_CHANNEL(API_KEY, channel_id)
    YT.get_channel_metadata()
    #YT.get_activities(2 * YT.num_vids)
    #YT.get_captions()
    #YT.get_channels()
    #YT.get_channel_sections()
    '''
    for vid_id in vid_ids:
        vid = YT.make_Comment(API_KEY, vid_id)
        vid.comment_ids = vid.get_vid_comment_ids()
        vid.get_vid_comments()
    '''
    #YT.get_playlists()
    #YT.get_playlist_items(2 * YT.num_vids)
    YT.get_related_vids()
    #YT.get_video()

if __name__ == "__main__":
    main()
