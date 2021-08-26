import os
import json
import requests
from datetime import date

class Activities():

    def get_activities(self, num_vids):
        parts = ["contentDetails", "id", "snippet"]
        for part in parts:
            self.get_part_activities(part, num_vids)

    def get_part_activities(self, part, num_vids):
        url = f"https://www.googleapis.com/youtube/v3/activities?part={part}&maxResults={num_vids}&channelId={self.channel_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_part_activities(results, part, num_vids)
        return

    def write_part_activities(self, results, part, num_vids):
        with open(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{date.today()}", "activity", f"{self.channel_name}_{part}_activities.json"), "w") as f:
            json.dump(results, f, indent = 4)
