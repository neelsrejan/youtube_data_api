import json
import requests

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
        with open(f"{vid_id}_{part}_video.json", "w") as f:
            json.dump(results, f, indent = 4)
