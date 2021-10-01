import os
import json
import requests

class Channels:

    def get_channels(self):
        parts = ["brandingSettings", "snippet", "statistics", "topicDetails"]
        for part in parts:
            self.get_part_channels(part)
    
    def get_part_channels(self, part):
        self.API_COST += 1
        url = f"https://www.googleapis.com/youtube/v3/channels?part={part}&id={self.channel_id}&key={self.API_KEY}"
        response = json.loads(requests.get(url).text)
        self.write_part_channels(part, response)
        return 

    def write_part_channels(self, part, response):
        with open(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{self.date}", "raw", "channels", f"{part}_channels.json"), "w") as f:
            json.dump(response, f, indent = 4)
