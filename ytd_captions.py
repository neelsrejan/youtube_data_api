import json
import requests

class Captions:

    def get_captions(self):
        parts = ["id", "snippet"]
        for part in parts:
            for vid_num in range(len(self.vid_ids)):
                self.get_part_captions(part, self.vid_ids[vid_num])
                #self.snippet_captions(self.vid_ids[vid_num])

    def get_part_captions(self, part, vid_id):
        url = f"https://www.googleapis.com/youtube/v3/captions?part={part}&videoId={vid_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_part_captions(results, part, vid_id)
        return

    def write_part_captions(self, results, part, vid_id):
        with open(f"{self.channel_name}_{part}_{vid_id}_captions.json", "w") as f:
            json.dump(results, f, indent = 4)

