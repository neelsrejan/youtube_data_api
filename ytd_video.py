import os
import json
import requests
from datetime import date

class Video():

    def get_video(self):
        parts = ["contentDetails", "fileDetails", "id", "liveStreamingDetails", "localizations", "player", "processingDetails", "recordingDetails", "snippet", "statistics", "status", "suggestions", "topicDetails"]
        for part in parts:
            for vid_id in self.vid_ids:
                self.get_part_video(part, vid_id)

    def get_part_video(self, part, vid_id):
        url = f"https://www.googleapis.com/youtube/v3/videos?part={part}&id={vid_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_part_video(part, vid_id, results)

    def write_part_video(self, part, vid_id, results):
        with open(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{date.today()}", "videos", f"{self.channel_name}_{part}_{vid_id}_video.json"), "w") as f:
            json.dump(results, f, indent = 4)
