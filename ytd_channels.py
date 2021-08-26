import os
import json
import requests
from datetime import date

class Channels:

    # This function does not use auditDetails as it requires an Oauth2 for the response to work
    def get_channels(self):
        parts = ["brandingSettings", "contentDetails", "contentOwnerDetails", "id", "localizations", "snippet", "statistics", "status", "topicDetails"]
        for part in parts:
            self.get_part_channels(part)
    
    def get_part_channels(self, part):
        url = f"https://www.googleapis.com/youtube/v3/channels?part={part}&id={self.channel_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_part_channels(part, results)
        return 

    def write_part_channels(self, part, results):
        with open(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{date.today()}", "channels", f"{self.channel_name}_{part}_channels.json"), "w") as f:
            json.dump(results, f, indent = 4)
