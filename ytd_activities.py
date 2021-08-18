import os 
import requests
import json

class Activities:

    def __init__(self, API_KEY, channel_id):
        self.API_KEY = API_KEY
        self.channel_id = channel_id
        self.channel_name = None
        self.content_details = None
        self.id = None
        self.snippet = None
        self.tot_activity = None


    def ask_for_which_activity(self, numResults):
        which_activity = input("Which activity do you want to see for the channel? \nType c for content details, i for id, and s for snippet ")[0].lower()
        if which_activity == 'c':
            self.list_content_details(numResults)
        elif which_activity == 'i':
            self.list_id(numResults)
        elif which_activity == 's':
            self.list_snippet(numResults)
        else:
            print("Invalid response, please enter a valid letter")
            self.ask_for_which_activity(numResults)

    def ask_for_num_activities(self):
        userVal = int(input(f"Choose how many activites you wish to see upto {self.tot_activity} "))
        if userVal <= self.tot_activity:
            return userVal
        else:
            print("Invalid response, please enter another number")
            self.ask_for_activity(self.tot_activity)

    def get_total_activities(self):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=snippet&maxResults=1&channelId={self.channel_id}&key={self.API_KEY}"
        results = json.loads(requests.get(url).text)
        self.tot_activity = int(results["pageInfo"]["totalResults"])
        self.channel_name = results["items"][0]["snippet"]["channelTitle"].replace(" ", "_")
        return
         
    def list_content_details(self, numResults):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=contentDetails&maxResults={numResults}&channelId={self.channel_id}&key={self.API_KEY}"
        self.content_details = json.loads(requests.get(url).text)
        self.write_content_details(numResults)
        return

    def list_id(self, numResults):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=id&maxResults={numResults}&channelId={self.channel_id}&key={self.API_KEY}"
        self.id = json.loads(requests.get(url).text)
        self.write_id(numResults)
        return

    def list_snippet(self, numResults):
        url = f"https://www.googleapis.com/youtube/v3/activities?part=snippet&maxResults={numResults}&channelId={self.channel_id}&key={self.API_KEY}"
        self.snippet = json.loads(requests.get(url).text)
        self.write_snippet(numResults)

    def write_content_details(self, numResults):
        with open(f"{self.channel_name}_content_details_{numResults}_activities.json", "w") as f:
            json.dump(self.content_details, f, indent = 4)

    def write_id(self, numResults):
        with open(f"{self.channel_name}_id_{numResults}_activities.json", "w") as f:
            json.dump(self.id, f, indent = 4)

    def write_snippet(self, numResults):
        with open(f"{self.channel_name}_snippet_{numResults}_activities.json", "w") as f:
            json.dump(self.snippet, f, indent = 4)
