import os
import json
import requests

class Video():

    def get_video(self, vid_id):
        parts = ["contentDetails", "snippet", "statistics"]
        for part in parts:
            self.get_part_video(part, vid_id)

    def get_num_comments(self, vid_id):
        self.API_COST += 1
        url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={vid_id}&key={self.API_KEY}"
        response = json.loads(requests.get(url).text)
        return response["items"][0]["statistics"]["commentCount"]

    def get_part_video(self, part, vid_id):
        self.API_COST += 1
        url = f"https://www.googleapis.com/youtube/v3/videos?part={part}&id={vid_id}&key={self.API_KEY}"
        response = json.loads(requests.get(url).text)
        self.write_part_video(part, vid_id, response)

    def write_part_video(self, part, vid_id, response):
        with open(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{self.date}", "raw", "videos", f"{vid_id}_{part}_video.json"), "w") as f:
            json.dump(response, f, indent = 4)
