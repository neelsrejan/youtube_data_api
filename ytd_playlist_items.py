import json
import requests

class Playlist_Items():

    def get_playlist_items(self, maxResults):
        parts = ["contentDetails", "id", "snippet", "status"]
        for part in parts:
            for playlist_id in self.playlist_ids:
                self.get_part_playlist_items(part, playlist_id, maxResults)

    def get_part_playlist_items(self, part, playlist_id, maxResults):
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?part={part}&playlistId={playlist_id}&maxResults={maxResults}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_part_playlist_items(part, playlist_id, results)

    def write_part_playlist_items(self, part, playlist_id, results):
        with open(f"{playlist_id}_{part}_playlist_items.json", "w") as f:
            json.dump(results, f, indent = 4)
