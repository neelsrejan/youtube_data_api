import os
import json
import requests
from datetime import date

class Comments():

    def get_comments(self):
        comment_dictionary = {"videoId": self.vid_id, "all_comments": []}
        for main_comment_id, thread_ids in self.comment_thread_ids:
            results = self.get_part_comment(main_comment_id)
            results["replies"] = []
            if len(thread_ids) != 0:
                for thread_id in thread_ids:
                    results["replies"].append(self.get_part_comment(thread_id))
                comment_dictionary["all_comments"].append(results)
            else:
                comment_dictionary["all_comments"].append(results)
        self.write_part_comment(comment_dictionary)

    def get_part_comment(self, comment_id):
        url = f"https://www.googleapis.com/youtube/v3/comments?part=snippet&id={comment_id}&key={self.API_KEY}"
        return json.loads(requests.get(url).text)

    def write_part_comment(self, comment_dictionary):
        with open(os.path.join(os.getcwd(), f"{self.channel_name}_data", f"{date.today()}", "comments", f"{self.channel_name}_{self.vid_id}_comments.json"), "w") as f:
            json.dump(comment_dictionary, f, indent = 4)
