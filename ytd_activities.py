import requests
import json

class Activities:

    def __init__(self, API_KEY, channel_id):
        self.API_KEY = API_KEY
        self.channel_id = channel_id
        self.channel_stats = None

    def list_content_details(self):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=snippet&id={self.channel_id}&key={self.API_KEY}"
        json_data = requests.get(url).text
        print(json_data)
        """
        data_dict = json.loads(json_data)
        try:
            stats = data_dict["items"][0]["statistics"]
        except:
            stats = None
        self.channel_stats = stats
        return

    def json_stats(self):
        with open("conceptNewEraOverview.json", "w") as f:
            json.dump(self.channel_stats, f, indent = 4)
       """
