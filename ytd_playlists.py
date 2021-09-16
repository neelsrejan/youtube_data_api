import os
import json
import requests
from datetime import date

class Playlists():

    def get_playlists(self):
        parts = ["contentDetails", "id", "localizations", "player", "snippet", "status"]
        for part in parts:
            self.get_part_playlists(part)

    def get_part_playlists(self, part):
        url = f"https://www.googleapis.com/youtube/v3/playlists?part={part}&channelId={self.channel_id}&maxResults=50&key={self.API_KEY}"
        response = json.loads(requests.get(url).text)
        to_write = response

        while 1:
            try:
                next_page_token = response["nextPageToken"]
                url = f"https://www.googleapis.com/youtube/v3/playlists?part={part}&channelId={self.channel_id}&maxResults=50&pageToken={next_page_token}&key={self.API_KEY}"
                response = json.loads(requests.get(url).text)
                for item in response["items"]
                    to_write["items"].append(item)
            except KeyError:
                break
        self.write_part_playlists(part, to_write)

    def write_part_playlists(self, part, to_write):
        with open(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{date.today()}", "playlists", f"{self.channel_name}_{part}_playlists.json"), "w") as f:
            json.dump(to_write, f, indent = 4)
