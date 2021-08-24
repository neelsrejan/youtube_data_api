import json
import requests

class Comment_Threads():

    def get_main_comment_ids(self):
        url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={self.vid_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        num_comments = results["pageInfo"]["totalResults"]
        return [results["items"][num_comment]["id"] for num_comment in range(num_comments)]

    def get_reply_ids(self, comment_id):
        url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=replies&id={comment_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        try:
            num_replies = len(results["items"][0]["replies"]["comments"])
            return [results["items"][0]["replies"]["comments"][num_reply]["id"] for num_reply in range(num_replies)]
        except KeyError:
            return []
