import requests
import json

class Activities():

    def get_activities(self, num_vids):
        self.list_content_details_activities(num_vids)
        self.list_id_activities(num_vids)
        self.list_snippet_activities(num_vids)

    def list_content_details_activities(self, num_vids):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=contentDetails&maxResults={num_vids}&channelId={self.channel_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_content_details_activities(results, num_vids)
        return

    def list_id_activities(self, num_vids):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=id&maxResults={num_vids}&channelId={self.channel_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_id_activities(results, num_vids)
        return

    def list_snippet_activities(self, num_vids):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=snippet&maxResults={num_vids}&channelId={self.channel_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.write_snippet_activities(results, num_vids)
        return

    def write_content_details_activities(self, results, num_vids):
        no_space_name = self.channel_name.replace(" ", "_")
        with open(f"{no_space_name}_content_details_{int(num_vids/2)}_activities.json", "w") as f:
            json.dump(results, f, indent = 4)

    def write_id_activities(self, results, num_vids):
        no_space_name = self.channel_name.replace(" ", "_")
        with open(f"{no_space_name}_id_{int(num_vids/2)}_activities.json", "w") as f:
            json.dump(results, f, indent = 4)

    def write_snippet_activities(self, results, num_vids):
        no_space_name = self.channel_name.replace(" ", "_")
        with open(f"{no_space_name}_snippet_{int(num_vids/2)}_activities.json", "w") as f:
            json.dump(results, f, indent = 4)
