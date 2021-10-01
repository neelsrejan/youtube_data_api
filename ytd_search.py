import os
import json
import requests
from datetime import date

class Search():

    def get_related_vids(self, vid_id):
        self.get_snippet_related_vids(vid_id)
          
    def get_snippet_related_vids(self, vid_id):
        self.API_COST += 100
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={self.channel_id}&relatedToVideoId={vid_id}&maxResults=50&type=video&key={self.API_KEY}"
        response = json.loads(requests.get(url).text)
        self.write_snippet_related_vids(vid_id, response)

    def write_snippet_related_vids(self, vid_id, response):
        with open(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{date.today()}", "search", f"{self.channel_name}_{vid_id}_related_videos.json"), "w") as f:
            json.dump(response, f, indent = 4)
