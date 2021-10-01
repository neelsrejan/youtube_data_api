import json
import requests

class Comment_Threads():

    def get_main_comment_ids(self):
        main_comment_ids = []
        self.COMMENT_API_COST += 1
        url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&order=time&maxResults=100&videoId={self.vid_id}&key={self.API_KEY}"
        response = json.loads(requests.get(url).text)
        for item in response["items"]:
            main_comment_ids.append(item["id"])
        while 1:
            try:
                next_page_token = response["nextPageToken"]
                self.COMMENT_API_COST += 1
                url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&&order=time&maxResults=100&pageToken={next_page_token}&videoId={self.vid_id}&key={self.API_KEY}"
                response = json.loads(requests.get(url).text)
                for item in response["items"]:
                    main_comment_ids.append(item["id"])
            except KeyError:
                break
        return main_comment_ids

    def get_reply_ids(self, comment_id):
        self.COMMENT_API_COST += 1
        url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=replies&id={comment_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        try:
            num_replies = len(results["items"][0]["replies"]["comments"])
            return [results["items"][0]["replies"]["comments"][num_reply]["id"] for num_reply in range(num_replies)]
        except KeyError:
            return []
