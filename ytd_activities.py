import requests
import json

class Activities():

    def get_activities(self, num_vids):
        self.vid_ids = self.list_content_details(num_vids)
        self.list_id(num_vids)
        self.list_snippet(num_vids)

    def list_content_details(self, num_vids):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=contentDetails&maxResults={num_vids}&channelId={self.channel_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_content_details(results, num_vids)
        ids = [item["contentDetails"]["upload"]["videoId"] for item in results["items"] if len(item["contentDetails"]) != 0]
        return ids

    def list_id(self, num_vids):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=id&maxResults={num_vids}&channelId={self.channel_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_id(results, num_vids)
        return

    def list_snippet(self, num_vids):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=snippet&maxResults={num_vids}&channelId={self.channel_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_snippet(results, num_vids)

    def write_content_details(self, results, num_vids):
        no_space_name = self.channel_name.replace(" ", "_")
        with open(f"{no_space_name}_content_details_{int(num_vids/2)}_activities.json", "w") as f:
            json.dump(results, f, indent = 4)

    def write_id(self, results, num_vids):
        no_space_name = self.channel_name.replace(" ", "_")
        with open(f"{no_space_name}_id_{int(num_vids/2)}_activities.json", "w") as f:
            json.dump(results, f, indent = 4)

    def write_snippet(self, results, num_vids):
        no_space_name = self.channel_name.replace(" ", "_")
        with open(f"{no_space_name}_snippet_{int(num_vids/2)}_activities.json", "w") as f:
            json.dump(results, f, indent = 4)
