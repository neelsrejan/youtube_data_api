import os
import json
import requests

class Playlist_Items():

    def get_playlist_items(self):
        for playlist_id in self.playlist_ids:
            self.get_part_playlist_items(playlist_id)

    def get_part_playlist_items(self, playlist_id):
        self.API_COST += 1
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_id}&maxResults=50&key={self.API_KEY}"
        response = json.loads(requests.get(url).text)
        to_write = response

        while 1:
            try:
                next_page_token = response["nextPageToken"]
                self.API_COST += 1
                url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={playlist_id}&maxResults=50&pageToken={next_page_token}&key={self.API_KEY}"
                response = json.loads(requests.get(url).text)
                for item in response["items"]:
                    to_write["items"].append(item)
            except KeyError:
                break
        self.write_part_playlist_items(playlist_id, to_write)

    def write_part_playlist_items(self, playlist_id, to_write):
        with open(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{self.date}", "raw", "playlist_items", f"{playlist_id}_snippet_playlist_items.json"), "w") as f:
            json.dump(to_write, f, indent = 4)
