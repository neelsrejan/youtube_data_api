import os
import json
import requests

class Search():

    def get_search(self, vid_id):
        self.get_part_search(vid_id)
          
    def get_part_search(self, vid_id):
        self.API_COST += 100
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={self.channel_id}&relatedToVideoId={vid_id}&maxResults=50&type=video&key={self.API_KEY}"
        response = json.loads(requests.get(url).text)
        self.write_part_search(vid_id, response)

    def write_part_search(self, vid_id, response):
        with open(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{self.date}", "raw", "search", f"{vid_id}_search.json"), "w") as f:
            json.dump(response, f, indent = 4)
