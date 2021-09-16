import os
import json
import requests
from datetime import date

class Playlist_Items():

    def get_playlist_items(self):
        parts = ["contentDetails", "id", "snippet", "status"]
        for part in parts:
            for playlist_id in self.playlist_ids:
                self.get_part_playlist_items(part, playlist_id)

    def get_part_playlist_items(self, part, playlist_id):
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part={part}&playlistId={playlist_id}&maxResults=50&key={self.API_KEY}"
        response = json.loads(requests.get(url).text)
        to_write = response

        while 1:
            try:
                next_page_token = response["nextPageToken"]
                url = f"https://www.googleapis.com/youtube/v3/playlistItems?part={part}&playlistId={playlist_id}&maxResults=50&pageToken={next_page_token}&key={self.API_KEY}"
                response = json.loads(requests.get(url).text)
                for item in response["items"]:
                    to_write["items"].append(item)
            except KeyError:
                break
        self.write_part_playlist_items(part, playlist_id, to_write)

    def write_part_playlist_items(self, part, playlist_id, to_write):
        with open(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{date.today()}", "playlist_items", f"{self.channel_name}_{part}_{playlist_id}_playlist_items.json"), "w") as f:
            json.dump(to_write, f, indent = 4)
