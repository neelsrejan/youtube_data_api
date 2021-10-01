import os
import json
import requests

class Activities():

    def get_activity(self):
        parts = ["contentDetails", "snippet"]
        for part in parts:
            self.get_part_activity(part)

    def get_part_activity(self, part):
        self.API_COST += 1
        url = f"https://www.googleapis.com/youtube/v3/activities?part={part}&maxResults=256&channelId={self.channel_id}&key={self.API_KEY}"
        response = json.loads(requests.get(url).text)
        to_write = response

        while 1:
            try:
                next_page_token = response["nextPageToken"]
                self.API_COST += 1
                url = f"https://www.googleapis.com/youtube/v3/activities?part={part}&maxResults=256&channelId={self.channel_id}&key={self.API_KEY}"
                response = json.loads(requests.get(url).text)
                for item in response["items"]:
                    to_write["items"].append(item)
            except KeyError:
                break
        self.write_part_activity(to_write, part)


    def write_part_activity(self, to_write, part):
        with open(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{self.date}", "raw", "activity", f"{part}_activity.json"), "w") as f:
            json.dump(to_write, f, indent = 4)
