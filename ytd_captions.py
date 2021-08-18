import requests
import json

class Captions:

    def __init__(self, API_KEY, channel_id, videoId):
        self.API_KEY = API_KEY
        self.channel_id = channel_id
        self.videoId = videoId
        self.id = None
        self.snippet = None
        self.channelName = None

    def get_channel_name(self):
        url = f"https://googleapis.com/youtube/v3/activities?part=snippet&maxResults=1&channelId={self.channelId}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.channelName = results["items"][0]["snippet"]["channelTitle"].replace(" ", "_")
        return

    def list_id(self):
        url = f"https://googleapis.com/youtube/v3/captions?part=id&videoId={self.videoId}&key={API_KEY}"
        self.captions = json.loads(requests.get(url).text)
        return 

    def list_snippet(self):
        url = f"https://googleapis.com/youtube/v3/captions?part=snippet&videoId={self.videoId}&key={API_KEY}"
        self.snippet = json.loads(requests.get(url).text)

    def write_id(self):
        with open(f"{self.channelName}_id_{self.videoId}_captions.json", "w") as f:
            json.dump(self.id, f, indent = 4)

    def write_snippet(self):
        with open(f"{self.channelName)_snippet_{self.videoId}_captions.json", "w") as f:
            json.dump(self.snippet, f, indent = 4)
