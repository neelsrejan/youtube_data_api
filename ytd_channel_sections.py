import os 
import json
import requests
from datetime import date

class Channel_Sections:

    def get_channel_sections(self):
        parts = ["contentDetails", "id", "snippet"]
        for part in parts:
            self.get_part_channel_sections(part)

    def get_part_channel_sections(self, part):
        url = f"https://www.googleapis.com/youtube/v3/channelSections?part={part}&channelId={self.channel_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_part_channel_sections(results, part)
        return

    def write_part_channel_sections(self, results, part):
        with open(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{date.today()}", "channel_sections", f"{self.channel_name}_{part}_channel_sections.json"), "w") as f:
            json.dump(results, f, indent = 4)

