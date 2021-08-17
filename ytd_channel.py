class Channel:

    def __init__(self):
        pass

    def get_yt_statistics(self):
        url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.API_KEY}"
        json_data = requests.get(url).text
        print(json_data)
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