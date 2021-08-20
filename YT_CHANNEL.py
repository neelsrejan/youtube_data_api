import requests
import json
from ytd_activities import Activities
from ytd_captions import Captions

class YT_CHANNEL(Activities, Captions):

    def __init__(self, API_KEY, channel_id):
        self.API_KEY = API_KEY
        self.channel_id = channel_id
        super()
        self.channel_name = None
        self.num_vids = None
        self.vid_ids = None
        self.playlist_ids = None

    def get_channel_metadata(self):
        self.get_num_vids()
        self.get_channel_name()
        self.get_vid_ids(2*self.num_vids)

    def get_num_vids(self):
        url = f"https://WWW.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.API_KEY}"
        self.num_vids = int(json.loads(requests.get(url).text)["items"][0]["statistics"]["videoCount"])
        return

    def get_channel_name(self):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=snippet&maxResults=1&channelId={self.channel_id}&key={self.API_KEY}"
        self.channel_name = json.loads(requests.get(url).text)["items"][0]["snippet"]["channelTitle"]
        return 

    def get_vid_ids(self, num_vids):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=contentDetails&maxResults={num_vids}&channelId={self.channel_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.vid_ids = [item["contentDetails"]["upload"]["videoId"] for item in results["items"] if len(item["contentDetails"]) != 0]
        return 
