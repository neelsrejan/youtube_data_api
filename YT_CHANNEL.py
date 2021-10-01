import json
import requests
from datetime import datetime
from ytd_activities import Activities
from ytd_channels import Channels
from ytd_channel_sections import Channel_Sections
from YT_COMMENTS import YT_COMMENTS
from ytd_playlists import Playlists
from ytd_playlist_items import Playlist_Items
from ytd_search import Search
from ytd_video import Video
#from clean_data import Clean_Data

class YT_CHANNEL(Activities, Channels, Channel_Sections, YT_COMMENTS, Playlists, Playlist_Items, Search, Video):

    def __init__(self, API_KEY, channel_id):
        self.API_KEY = API_KEY
        self.channel_id = channel_id
        self.API_COST = 0
        super()
        self.channel_name = None
        self.num_vids = None
        self.vid_ids = [] 
        self.playlist_ids = []

    def make_comment(self, API_KEY, vid_id, channel_name):
        return YT_COMMENTS(API_KEY, vid_id, channel_name)

    def get_channel_metadata(self):
        self.get_num_vids()
        self.get_channel_name()
        self.get_vid_ids(self.num_vids)
        self.get_playlist_ids()

    def get_num_vids(self):
        self.API_COST += 1
        url = f"https://WWW.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.API_KEY}"
        self.num_vids = int(json.loads(requests.get(url).text)["items"][0]["statistics"]["videoCount"])
        return

    def get_channel_name(self):
        self.API_COST += 1
        url = f"https://www.googleapis.com/youtube/v3/activities?part=snippet&channelId={self.channel_id}&key={self.API_KEY}"
        self.channel_name = json.loads(requests.get(url).text)["items"][0]["snippet"]["channelTitle"].replace(" ", "_")
        return 

    def get_vid_ids(self, num_vids):
        date_of_vid = datetime.now().isoformat()[:21] + "Z"
        last_vid_id = ""

        while len(self.vid_ids) < num_vids:
            self.API_COST += 1
            url = f"https://www.googleapis.com/youtube/v3/activities?part=contentDetails&channelId={self.channel_id}&maxResults=256&publishedBefore={date_of_vid}&key={self.API_KEY}"
            response = json.loads(requests.get(url).text)
            for item in response["items"]:
                if len(item["contentDetails"]) != 0:
                    try:
                        if item["contentDetails"]["upload"]["videoId"] not in self.vid_ids:
                            self.vid_ids.append(item["contentDetails"]["upload"]["videoId"])
                    except KeyError:
                        if item["contentDetails"]["playlistItem"]["resourceId"]["videoId"] not in self.vid_ids:
                            self.vid_ids.append(item["contentDetails"]["playlistItem"]["resourceId"]["videoId"])

            if last_vid_id == self.vid_ids[-1]:
                break
            else:
                last_vid_id = self.vid_ids[-1]
                self.API_COST += 1
                url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={last_vid_id}&key={self.API_KEY}"
                date_of_vid = json.loads(requests.get(url).text)["items"][0]["snippet"]["publishedAt"]
        return

    def get_playlist_ids(self):
        self.API_COST += 1
        url = f"https://www.googleapis.com/youtube/v3/playlists?part=id&channelId={self.channel_id}&maxResults=50&key={self.API_KEY}"
        response = json.loads(requests.get(url).text)
        if len(response["items"]) != 0:
            for item in response["items"]:
                self.playlist_ids.append(item["id"])

        while 1:
            try:
                next_page_token = response["nextPageToken"]
                self.API_COST += 1
                url = f"https://www.googleapis.com/youtube/v3/playlists?part=id&channelId={self.channel_id}&maxResults=50&pageToken={next_page_token}&key={self.API_KEY}"
                response = json.loads(requests.get(url).text)
                if len(response["items"]) != 0:
                    for item in response["items"]:
                        self.playlist_ids.append(item["id"])
            except KeyError:
                break
        return
