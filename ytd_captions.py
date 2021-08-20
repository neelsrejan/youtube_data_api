import requests
import json

class Captions:

    def get_captions(self):
        for vid_num in range(len(self.vid_ids)):
            self.list_id_captions(self.vid_ids[vid_num])
            self.list_snippet_captions(self.vid_ids[vid_num])

    def list_id_captions(self, vid_id):
        url = f"https://www.googleapis.com/youtube/v3/captions?part=id&videoId={vid_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_id_captions(results, vid_id)
        return 

    def list_snippet_captions(self, vid_id):
        url = f"https://www.googleapis.com/youtube/v3/captions?part=snippet&videoId={vid_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_snippet_captions(results, vid_id)
        return

    def write_id_captions(self, results, vid_id):
        no_space_name = self.channel_name.replace(" ", "_")
        with open(f"{no_space_name}_id_{vid_id}_captions.json", "w") as f:
            json.dump(results, f, indent = 4)

    def write_snippet_captions(self, results, vid_id):
        no_space_name = self.channel_name.replace(" ", "_")
        with open(f"{no_space_name}_snippet_{vid_id}_captions.json", "w") as f:
            json.dump(results, f, indent = 4)
