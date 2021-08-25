import json
import requests
from ytd_activities import Activities
from ytd_captions import Captions
from ytd_channels import Channels
from ytd_channel_sections import Channel_Sections
from YT_COMMENTS import YT_COMMENTS
from ytd_playlists import Playlists
from ytd_playlist_items import Playlist_Items
from ytd_search import Search
from ytd_video import Video

class YT_CHANNEL(Activities, Captions, Channels, Channel_Sections, YT_COMMENTS, Playlists, Playlist_Items, Search, Video):

    def __init__(self, API_KEY, channel_id):
        self.API_KEY = API_KEY
        self.channel_id = channel_id
        super()
        self.channel_name = None
        self.num_vids = None
        self.vid_ids = None
        self.playlist_ids = None

    def make_Comment(self, API_KEY, vid_id):
        return YT_COMMENTS(API_KEY, vid_id)

    def get_channel_metadata(self):
        self.get_num_vids()
        self.get_channel_name()
        self.get_vid_ids(2 * self.num_vids)
        self.get_playlist_ids(2 * self.num_vids)

    def get_num_vids(self):
        url = f"https://WWW.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.API_KEY}"
        self.num_vids = int(json.loads(requests.get(url).text)["items"][0]["statistics"]["videoCount"])
        return

    def get_channel_name(self):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=snippet&maxResults=1&channelId={self.channel_id}&key={self.API_KEY}"
        self.channel_name = json.loads(requests.get(url).text)["items"][0]["snippet"]["channelTitle"].replace(" ", "_")
        return 

    def get_vid_ids(self, num_vids):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=contentDetails&maxResults={num_vids}&channelId={self.channel_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.vid_ids = [item["contentDetails"]["upload"]["videoId"] for item in results["items"] if len(item["contentDetails"]) != 0]
        return

    def get_playlist_ids(self, num_vids):
        url = f"https://www.googleapis.com/youtube/v3/playlists?part=id&channelId={self.channel_id}&maxResults={num_vids}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.playlist_ids = [playlist["id"] for playlist in results["items"] if len(results["items"]) != 0]
