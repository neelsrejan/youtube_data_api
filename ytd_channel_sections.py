import os 
import json
import requests
from datetime import date

class Channel_Sections:

    def get_channel_sections(self):
        parts = ["contentDetails", "snippet"]
        for part in parts:
            self.get_part_channel_sections(part)

    def get_part_channel_sections(self, part):
        self.API_COST += 1
        url = f"https://www.googleapis.com/youtube/v3/channelSections?part={part}&channelId={self.channel_id}&key={self.API_KEY}"
        response = json.loads(requests.get(url).text)
        self.write_part_channel_sections(response, part)
        return

    def write_part_channel_sections(self, response, part):
        with open(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{date.today()}", "channel_sections", f"{self.channel_name}_{part}_channel_sections.json"), "w") as f:
            json.dump(response, f, indent = 4)

