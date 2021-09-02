import os
import json
import pandas as pd

def main():
    #clean_activity()
    #clean_channel_sections()
    #clean_channels()
    clean_comments()

def clean_activity():
    content_detail_clean_data = []
    snippet_clean_data = []

    with open(os.path.join(os.getcwd(), "Concept_New_Era_data", "2021-08-26", "activity", "Concept_New_Era_contentDetails_activities.json"), "r") as f:
        data = json.load(f)
        for item in data["items"]:
            if item["contentDetails"] != {}:
                content_detail_clean_data.append([item["id"], item["contentDetails"]["upload"]["videoId"]])

    with open(os.path.join(os.getcwd(), "Concept_New_Era_data", "2021-08-26", "activity", "Concept_New_Era_snippet_activities.json"), "r") as f:
        data = json.load(f)
        for item in data["items"]:
            snippet_clean_data.append([item["id"], item["snippet"]["publishedAt"], item["snippet"]["channelId"], item["snippet"]["title"], item["snippet"]["description"], item["snippet"]["thumbnails"]["default"]["url"], item["snippet"]["channelTitle"], item["snippet"]["type"]])

    content_detail_df = pd.DataFrame(data=content_detail_clean_data, columns=["Activity_Id", "Video_Id"])
    snippet_df = pd.DataFrame(data=snippet_clean_data, columns=["Activity_Id", "Date_Published", "Channel_Id", "Video_Title", "Video_Description", "Thumbnail_default_url", "Channel_Name", "Activity_Type"])

    activity_df = content_detail_df.merge(snippet_df, on=["Activity_Id"], how="outer")
    
    activity_df.to_csv("clean_activity.csv", index=False)
    activity_df.to_excel("clean_activity.xlsx", index=False)

def clean_channel_sections():
    content_details_clean_data = []
    snippet_clean_data = []

    with open(os.path.join(os.getcwd(), "Concept_New_Era_data", "2021-08-26", "channel_sections", "Concept_New_Era_contentDetails_channel_sections.json"), "r") as f:
        data = json.load(f)
        for item in data["items"]:
            try:
                content_details_clean_data.append([item["id"], item["contentDetails"]["playlists"][0]])
            except KeyError:
                content_details_clean_data.append([item["id"], "None"])
    
    with open(os.path.join(os.getcwd(), "Concept_New_Era_data", "2021-08-26", "channel_sections", "Concept_New_Era_snippet_channel_sections.json"), "r") as f:
        data = json.load(f)
        for item in data["items"]:
            if item["snippet"]["type"] == "channelsectiontypeundefined":
                snippet_clean_data.append([item["id"], "youtube shorts", item["snippet"]["channelId"], item["snippet"]["position"]])
            else:
                snippet_clean_data.append([item["id"], item["snippet"]["type"], item["snippet"]["channelId"], item["snippet"]["position"]])

    content_details_df = pd.DataFrame(data=content_details_clean_data, columns=["Channel_Section_Id", "Playlist_Id"])
    snippet_df = pd.DataFrame(data=snippet_clean_data, columns=["Channel_Section_Id", "Type_Of_Section", "Channel_Id", "Position_On_Page"])

    channel_sections_df = content_details_df.merge(snippet_df, on=["Channel_Section_Id"], how="outer")
    channel_sections_df.to_csv("clean_channel_sections.csv", index=False)
    channel_sections_df.to_excel("clean_channel_sections.xlsx", index=False)

def clean_channels():
    branding_settings_clean_data = []
    snippet_clean_data = []
    statistics_clean_data = []
    topic_details_clean_data = []

    with open(os.path.join(os.getcwd(), "Concept_New_Era_data", "2021-08-26", "channels", "Concept_New_Era_brandingSettings_channels.json"), "r") as f:
        data = json.load(f)["items"][0]
        branding_settings_clean_data.append([data["id"], data["brandingSettings"]["channel"]["title"], data["brandingSettings"]["channel"]["description"], data["brandingSettings"]["image"]["bannerExternalUrl"]])

    with open(os.path.join(os.getcwd(), "Concept_New_Era_data", "2021-08-26", "channels", "Concept_New_Era_snippet_channels.json"), "r") as f:
       data = json.load(f)["items"][0]
       snippet_clean_data.append([data["id"], data["snippet"]["title"], data["snippet"]["description"], data["snippet"]["customUrl"], data["snippet"]["publishedAt"], data["snippet"]["thumbnails"]["default"], data["snippet"]["country"]])

    with open(os.path.join(os.getcwd(), "Concept_New_Era_data", "2021-08-26", "channels", "Concept_New_Era_statistics_channels.json"), "r") as f:
        data = json.load(f)["items"][0]
        statistics_clean_data.append([data["id"], data["statistics"]["viewCount"], data["statistics"]["subscriberCount"], data["statistics"]["videoCount"]])

    topic_ids = {"/m/04rlf": "Music", "/m/05fw6t": "Children's music", "/m/02mscn": "Christian music", "/m/0ggq0m": "Classical music", "/m/01lyv": "Country", "/m/02lkt": "Electronic music", "/m/0glt670": "Hip hop music", "/m/05rwpb": "Independent music", "/m/03_d0": "Jazz", "/m/028sqc": "Music of Asia", "/m/0g293": "Music of Latin America", "/m/064t9": "Pop music", "/m/06cqb": "Reggae", "/m/06j6l": "Rhythm and blues", "/m/06by7": "Rock music", "/m/0gywn": "Soul music", "/m/0bzvm2": "Gaming", "/m/025zzc": "Action game", "/m/02ntfj": "Action-adventure game", "/m/0b1vjn": "Casual game", "/m/02hygl": "Music video game", "/m/04q1x3q": "Puzzle video game", "/m/01sjng": "Racing video game", "/m/0403l3g": "Role-playing video game", "/m/021bp2": "Simulation video game", "/m/022dc6": "Sports game", "/m/03hf_rm": "Strategy video game", "/m/06ntj": "Sports", "/m/0jm_": "American football", "/m/018jz": "Baseball", "/m/018w8": "Basketball", "/m/01cgz": "Boxing", "/m/09xp_": "Cricket", "/m/02vx4": "Football", "/m/037hz": "Golf", "/m/03tmr": "Ice hockey", "/m/01h7lh": "Mixed martial arts", "/m/0410tth": "Motorsport", "/m/066wd": "Professional wrestling", "/m/07bs0": "Tennis", "/m/07_53": "Volleyball", "/m/02jjt": "Entertainment", "/m/095bb": "Animated cartoon", "/m/09kqc": "Humor", "/m/02vxn": "Movies", "/m/05qjc": "Performing arts", "/m/019_rr": "Lifestyle", "/m/032tl": "Fashion", "/m/027x7n": "Fitness", "/m/02wbm": "Food", "/m/0kt51": "Health", "/m/03glg": "Hobby", "/m/068hy": "Pets", "/m/041xxh": "Beauty", "/m/07c1v": "Technology", "/m/07bxq": "Tourism", "/m/07yv9": "Vehicles", "/m/01k8wb": "Knowledge", "/m/098wr": "Society"}
    with open(os.path.join(os.getcwd(), "Concept_New_Era_data", "2021-08-26", "channels", "Concept_New_Era_topicDetails_channels.json"), "r") as f:
        data = json.load(f)["items"][0]
        if len(data["topicDetails"]["topicIds"]) == 0:
            topic_details_clean_data.append([data["id"], "None"])
        else:
            for category in data["topicDetails"]["topicIds"]:
                topic_details_clean_data.append([data["id"], topic_ids[category]])

    branding_settings_df = pd.DataFrame(data=branding_settings_clean_data, columns=["Channel_Id", "Channel_Name", "Channel_Description", "Channel_Banner_Url"])
    snippet_df = pd.DataFrame(data=snippet_clean_data, columns=["Channel_Id", "Channel_Name", "Channel_Description", "Custom_Url", "Channel_Start_Date", "Thumbnail_Url", "Country"])
    statistics_df = pd.DataFrame(data=statistics_clean_data, columns=["Channel_Id", "Channel_Total_Views", "Channel_Subscriber_Count", "Channel_Total_Videos"])
    topic_details_df = pd.DataFrame(data=topic_details_clean_data, columns=["Channel_Id", "Channel Category"])

    temp_df = branding_settings_df.merge(snippet_df, on=["Channel_Id"], how="outer")
    channels_df = temp_df.merge(topic_details_df, on=["Channel_Id"], how="outer")

    channels_df.to_csv("clean_channels.csv", index=False)
    channels_df.to_excel("clean_channels.xlsx", index=False)

def clean_comments():
    clean_comments_data = []
    
    with open(os.path.join(os.getcwd(), "Concept_New_Era_data", "2021-09-01", "comments", "Concept_New_Era_xzn1JjU-0G0_comments.json"), "r") as f:
        data = json.load(f)
        if len(data["all_comments"]) == 0:
            clean_comments_data.append([data["videoId"], "NULL", "NULL"])
        else:
            max_replies = 0
            for comment_thread in data["all_comments"]:
                if len(comment_thread["replies"]) > max_replies:
                    max_replies = len(comment_thread["replies"])

            for comment_thread in data["all_comments"]:
                main_comment = comment_thread["items"][0]["snippet"]
                if len(comment_thread["replies"]) == 0:
                        clean_comments_data.append([data["videoId"], main_comment["authorDisplayName"], main_comment["authorChannelUrl"], main_comment["textOriginal"], main_comment["likeCount"], main_comment["publishedAt"]])
                else:
                    to_append = [data["videoId"], main_comment["authorDisplayName"], main_comment["authorChannelUrl"], main_comment["textOriginal"], main_comment["likeCount"], main_comment["publishedAt"]]
                    replies = comment_thread["replies"]
                    
                    if len(comment_thread["replies"]) != max_replies:
                        num_null_loops = max_replies - len(comment_thread["replies"])
                        for i in range(len(comment_thread["replies"])):
                            to_append.append(replies[i]["items"][0]["snippet"]["authorDisplayName"])
                            to_append.append(replies[i]["items"][0]["snippet"]["authorChannelUrl"])
                            to_append.append(replies[i]["items"][0]["snippet"]["textOriginal"])
                            to_append.append(replies[i]["items"][0]["snippet"]["likeCount"])
                            to_append.append(replies[i]["items"][0]["snippet"]["publishedAt"])
                        for i in range(5*num_null_loops):
                            to_append.append("Null")
                    else:
                        for i in range(len(comment_thread["replies"])):
                            to_append.append(replies[i]["items"][0]["snippet"]["authorDisplayName"])
                            to_append.append(replies[i]["items"][0]["snippet"]["authorChannelUrl"])
                            to_append.append(replies[i]["items"][0]["snippet"]["textOriginal"])
                            to_append.append(replies[i]["items"][0]["snippet"]["likeCount"])
                            to_append.append(replies[i]["items"][0]["snippet"]["publishedAt"])
                         
if __name__ == "__main__":
    main()
