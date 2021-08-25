import json
import requests

class Playlists():

    def get_playlists(self):
        parts = ["contentDetails", "id", "localizations", "player", "snippet", "status"]
        for part in parts:
            self.get_part_playlists(part)

    def get_part_playlists(self, part):
        url = f"https://www.googleapis.com/youtube/v3/playlists?part={part}&channelId={self.channel_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_part_playlists(part, results)

    def write_part_playlists(self, part, results):
        with open(f"{self.channel_name}_{part}_playlists.json", "w") as f:
            json.dump(results, f, indent = 4)
