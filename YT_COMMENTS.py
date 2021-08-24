from ytd_comment_threads import Comment_Threads
from ytd_comments import Comments

class YT_COMMENTS(Comment_Threads, Comments):

    def __init__(self, API_KEY, vid_id):
        self.API_KEY = API_KEY
        self.vid_id = vid_id
        super()
        self.comment_ids = None
        self.reply_ids = None
        self.comment_thread_ids = []

    def get_vid_comment_ids(self):
        self.comment_ids = self.get_main_comment_ids()
        for comment_id in self.comment_ids:
            self.reply_ids = self.get_reply_ids(comment_id)
            self.comment_thread_ids.append([comment_id, self.reply_ids])

    def get_vid_comments(self):
        self.get_comments()
