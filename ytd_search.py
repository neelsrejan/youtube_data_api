import os
import json
import requests
from datetime import date

class Search():

    def get_related_vids(self):
        for vid_id in self.vid_ids:
            self.get_snippet_related_vids(vid_id)
          
    def get_snippet_related_vids(self, vid_id):
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={self.channel_id}&relatedToVideoId={vid_id}&maxResults=50&type=video&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_snippet_related_vids(vid_id, results)

    def write_snippet_related_vids(self, vid_id, results):
        with open(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{date.today()}", "search", f"{self.channel_name}_{vid_id}_related_videos.json"), "w") as f:
            json.dump(results, f, indent = 4)
