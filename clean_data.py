import os
import json
import time
import pandas as pd

def clean_data(channel_name, vid_ids, playlist_ids, date):
    clean_activity(channel_name, date)
    clean_channel_sections(channel_name, date)
    clean_channels(channel_name, date)
    time.sleep(60)
    clean_comments(channel_name, vid_ids, date)
    clean_playlist_items(channel_name, playlist_ids, date)
    clean_playlists(channel_name, date)
    clean_search(channel_name, vid_ids, date)
    clean_videos(channel_name, vid_ids, date)

def clean_activity(channel_name, date):
    content_detail_clean_data = []
    snippet_clean_data = []

    with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "activity", "contentDetails_activity.json"), "r") as f:
        data = json.load(f)
        for item in data["items"]:
            if item["contentDetails"] != {}:
                content_detail_clean_data.append([item["id"], item["contentDetails"]["upload"]["videoId"]])

    with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "activity", "snippet_activity.json"), "r") as f:
        data = json.load(f)
        for item in data["items"]:
            snippet_clean_data.append([item["id"], item["snippet"]["publishedAt"], item["snippet"]["channelId"], item["snippet"]["title"], item["snippet"]["description"], item["snippet"]["thumbnails"]["default"]["url"], item["snippet"]["channelTitle"], item["snippet"]["type"]])

    content_detail_df = pd.DataFrame(data=content_detail_clean_data, columns=["Activity_Id", "Video_Id"])
    snippet_df = pd.DataFrame(data=snippet_clean_data, columns=["Activity_Id", "Date_Published", "Channel_Id", "Video_Title", "Video_Description", "Thumbnail_default_url", "Channel_Name", "Activity_Type"])

    activity_df = content_detail_df.merge(snippet_df, on=["Activity_Id"], how="outer")
    
    activity_df.to_csv(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "csv", "activity", "activity.csv"), index=False)
    activity_df.to_excel(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "xlsx", "activity", "activity.xlsx"), index=False)

def clean_channel_sections(channel_name, date):
    content_details_clean_data = []
    snippet_clean_data = []

    with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "channel_sections", "contentDetails_channel_sections.json"), "r") as f:
        data = json.load(f)
        for item in data["items"]:
            try:
                content_details_clean_data.append([item["id"], item["contentDetails"]["playlists"][0]])
            except KeyError:
                content_details_clean_data.append([item["id"], "NULL"])
    
    with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "channel_sections", "snippet_channel_sections.json"), "r") as f:
        data = json.load(f)
        for item in data["items"]:
            if item["snippet"]["type"] == "channelsectiontypeundefined":
                snippet_clean_data.append([item["id"], "youtube shorts", item["snippet"]["channelId"], item["snippet"]["position"]])
            else:
                snippet_clean_data.append([item["id"], item["snippet"]["type"], item["snippet"]["channelId"], item["snippet"]["position"]])

    content_details_df = pd.DataFrame(data=content_details_clean_data, columns=["Channel_Section_Id", "Playlist_Id"])
    snippet_df = pd.DataFrame(data=snippet_clean_data, columns=["Channel_Section_Id", "Type_Of_Section", "Channel_Id", "Position_On_Page"])

    channel_sections_df = content_details_df.merge(snippet_df, on=["Channel_Section_Id"], how="outer")
    channel_sections_df.to_csv(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "csv", "channel_sections", "channel_sections.csv"), index=False)
    channel_sections_df.to_excel(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "xlsx", "channel_sections", "channel_sections.xlsx"), index=False)

def clean_channels(channel_name, date):
    branding_settings_clean_data = []
    snippet_clean_data = []
    statistics_clean_data = []
    topic_details_clean_data = []

    with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "channels", "brandingSettings_channels.json"), "r") as f:
        data = json.load(f)["items"][0]
        branding_settings_clean_data.append([data["id"], data["brandingSettings"]["channel"]["title"], data["brandingSettings"]["channel"]["description"], data["brandingSettings"]["image"]["bannerExternalUrl"]])

    with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "channels", "snippet_channels.json"), "r") as f:
       data = json.load(f)["items"][0]
       snippet_clean_data.append([data["id"], data["snippet"]["title"], data["snippet"]["description"], data["snippet"]["customUrl"], data["snippet"]["publishedAt"], data["snippet"]["thumbnails"]["default"], data["snippet"]["country"]])

    with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "channels", "statistics_channels.json"), "r") as f:
        data = json.load(f)["items"][0]
        statistics_clean_data.append([data["id"], data["statistics"]["viewCount"], data["statistics"]["subscriberCount"], data["statistics"]["videoCount"]])

    topic_ids = {"/m/04rlf": "Music", "/m/05fw6t": "Children's music", "/m/02mscn": "Christian music", "/m/0ggq0m": "Classical music", "/m/01lyv": "Country", "/m/02lkt": "Electronic music", "/m/0glt670": "Hip hop music", "/m/05rwpb": "Independent music", "/m/03_d0": "Jazz", "/m/028sqc": "Music of Asia", "/m/0g293": "Music of Latin America", "/m/064t9": "Pop music", "/m/06cqb": "Reggae", "/m/06j6l": "Rhythm and blues", "/m/06by7": "Rock music", "/m/0gywn": "Soul music", "/m/0bzvm2": "Gaming", "/m/025zzc": "Action game", "/m/02ntfj": "Action-adventure game", "/m/0b1vjn": "Casual game", "/m/02hygl": "Music video game", "/m/04q1x3q": "Puzzle video game", "/m/01sjng": "Racing video game", "/m/0403l3g": "Role-playing video game", "/m/021bp2": "Simulation video game", "/m/022dc6": "Sports game", "/m/03hf_rm": "Strategy video game", "/m/06ntj": "Sports", "/m/0jm_": "American football", "/m/018jz": "Baseball", "/m/018w8": "Basketball", "/m/01cgz": "Boxing", "/m/09xp_": "Cricket", "/m/02vx4": "Football", "/m/037hz": "Golf", "/m/03tmr": "Ice hockey", "/m/01h7lh": "Mixed martial arts", "/m/0410tth": "Motorsport", "/m/066wd": "Professional wrestling", "/m/07bs0": "Tennis", "/m/07_53": "Volleyball", "/m/02jjt": "Entertainment", "/m/095bb": "Animated cartoon", "/m/09kqc": "Humor", "/m/02vxn": "Movies", "/m/05qjc": "Performing arts", "/m/019_rr": "Lifestyle", "/m/032tl": "Fashion", "/m/027x7n": "Fitness", "/m/02wbm": "Food", "/m/0kt51": "Health", "/m/03glg": "Hobby", "/m/068hy": "Pets", "/m/041xxh": "Beauty", "/m/07c1v": "Technology", "/m/07bxq": "Tourism", "/m/07yv9": "Vehicles", "/m/01k8wb": "Knowledge", "/m/098wr": "Society"}

    with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "channels", "topicDetails_channels.json"), "r") as f:
        data = json.load(f)["items"][0]
        if len(data["topicDetails"]["topicIds"]) == 0:
            topic_details_clean_data.append([data["id"], "NULL"])
        else:
            for category in data["topicDetails"]["topicIds"]:
                topic_details_clean_data.append([data["id"], topic_ids[category]])

    branding_settings_df = pd.DataFrame(data=branding_settings_clean_data, columns=["Channel_Id", "Channel_Name", "Channel_Description", "Channel_Banner_Url"])
    snippet_df = pd.DataFrame(data=snippet_clean_data, columns=["Channel_Id", "Channel_Name", "Channel_Description", "Custom_Url", "Channel_Start_Date", "Thumbnail_Url", "Country"])
    statistics_df = pd.DataFrame(data=statistics_clean_data, columns=["Channel_Id", "Channel_Total_Views", "Channel_Subscriber_Count", "Channel_Total_Videos"])
    topic_details_df = pd.DataFrame(data=topic_details_clean_data, columns=["Channel_Id", "Channel_Category"])

    temp_df = branding_settings_df.merge(snippet_df, on=["Channel_Id", "Channel_Name", "Channel_Description"], how="outer")
    channels_df = temp_df.merge(topic_details_df, on=["Channel_Id"], how="outer")

    channels_df.to_csv(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "csv", "channels", "channels.csv"), index=False)
    channels_df.to_excel(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "xlsx", "channels", "channels.xlsx"), index=False)

def clean_comments(channel_name, vid_ids, date):
    unordered_df_sizes = []
    for vid_id in vid_ids:
        with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "comments", f"{vid_id}_comments.json"), "r") as f:
            data = json.load(f)
            if len(data["all_comments"]) == 0:
                clean_comments_df = pd.DataFrame({"Video_Id": data["videoId"], "Main_Comment": "Null", "Replies": "Null"})
                list_to_order.append((-len(clean_comments_df.columns), clean_comments_df))
                pq.put((-len(clean_comments_df.columns), clean_comments_df))
                clean_comments_df.to_csv(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "csv", "comments", f"{vid_id}_comments.csv"), index=False, na_rep="Null")
                clean_comments_df.to_excel(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "xlsx", "comments", f"{vid_id}_comments.xlsx"), index=False, na_rep="Null")
            else:
                max_replies = 0
                for comment_thread in data["all_comments"]:
                    if len(comment_thread["replies"]) > max_replies:
                        max_replies = len(comment_thread["replies"])

                clean_comments_df = pd.DataFrame(columns=["Video_Id"])

                for i in range(max_replies + 1):
                    clean_comments_df[f"Author_Name_{i}"] = None
                    clean_comments_df[f"Author_YT_Channel_Url_{i}"] = None
                    clean_comments_df[f"Comment_{i}"] = None
                    clean_comments_df[f"Likes_{i}"] = None
                    clean_comments_df[f"Date_Published_{i}"] = None

                for comment_thread_num in range(len(data["all_comments"])):
                    main_comment = data["all_comments"][comment_thread_num]["items"][0]["snippet"]
                    replies = data["all_comments"][comment_thread_num]["replies"]
                    to_append = [data["videoId"], main_comment["authorDisplayName"], main_comment["authorChannelUrl"], main_comment["textOriginal"], main_comment["likeCount"], main_comment["publishedAt"]]

                    if len(replies) == 0:
                        for i in range(5*max_replies):
                            to_append.append("Null")
                    else:
                        for i in range(len(replies)):
                            to_append.append(replies[i]["items"][0]["snippet"]["authorDisplayName"])
                            to_append.append(replies[i]["items"][0]["snippet"]["authorChannelUrl"])
                            to_append.append(replies[i]["items"][0]["snippet"]["textOriginal"])
                            to_append.append(replies[i]["items"][0]["snippet"]["likeCount"])
                            to_append.append(replies[i]["items"][0]["snippet"]["publishedAt"])
                        for i in range(5*(max_replies-len(replies))):
                            to_append.append("Null")
                    clean_comments_df.loc[len(clean_comments_df)] = to_append

                unordered_df_sizes.append((-len(clean_comments_df.columns), clean_comments_df))
    
    ordered_df_sizes = sorted(unordered_df_sizes, key=lambda x:x[0])
    
    super_df = ordered_df_sizes[0][1]
    del ordered_df_sizes[0]
    for curr_df in ordered_df_sizes:
        super_df = super_df.append(curr_df[1], ignore_index=True)

    super_df.to_csv(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "csv", "comments", "comments.csv"), index=False, na_rep="Null")
    super_df.to_excel(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "xlsx", "comments", "comments.xlsx"), index=False, na_rep="Null")

def clean_playlist_items(channel_name, playlist_ids, date):
    all_playlist_items = []
    for playlist_id in playlist_ids:
        clean_snippet_data = []
        with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "playlist_items", f"{playlist_id}_snippet_playlist_items.json"), "r") as f:
            data = json.load(f)
            for item in data["items"]:
                clean_snippet_data.append([item["snippet"]["channelId"], item["snippet"]["channelTitle"], item["snippet"]["playlistId"], item["snippet"]["position"], item["snippet"]["resourceId"]["videoId"], item["snippet"]["publishedAt"], item["snippet"]["title"], item["snippet"]["description"], item["snippet"]["thumbnails"]["default"]["url"]])

        clean_snippet_df = pd.DataFrame(data=clean_snippet_data, columns=["Channel_Id", "Channel_Name", "Playlist_Id", "Playlist_position", "Video_Id", "Video_Published_At", "Video_Title", "Video_Description", "Default_Thumbnail_Url"])
        all_playlist_items.append(clean_snippet_df)

    super_df = all_playlist_items[0]
    del all_playlist_items[0]
    for curr_df in all_playlist_items:
        super_df = super_df.append(curr_df)

    super_df.to_csv(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "csv", "playlist_items", f"playlist_items.csv"), index=False)
    super_df.to_excel(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "xlsx", "playlist_items", f"playlist_items.xlsx"), index=False)

def clean_playlists(channel_name, date):
    clean_content_details_data = []
    clean_player_data = []
    clean_snippet_data = []

    with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "playlists", "contentDetails_playlists.json"), "r") as f:
        data = json.load(f)
        for item in data["items"]:
            clean_content_details_data.append([item["id"], item["contentDetails"]["itemCount"]])

    with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "playlists", "player_playlists.json"), "r") as f:
        data = json.load(f)
        for item in data["items"]:
            url = item["player"]["embedHtml"].split()[3][5:-1]
            clean_player_data.append([item["id"], item["player"]["embedHtml"], url])
    
    with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "playlists", "snippet_playlists.json"), "r") as f:
        data = json.load(f)
        for item in data["items"]:
            clean_snippet_data.append([item["id"], item["snippet"]["channelId"], item["snippet"]["channelTitle"], item["snippet"]["publishedAt"], item["snippet"]["title"], item["snippet"]["description"], item["snippet"]["thumbnails"]["default"]["url"]])

    clean_content_details_df = pd.DataFrame(data=clean_content_details_data, columns=["Playlist_Id", "Videos_In_Playlist"])
    clean_player_df = pd.DataFrame(data=clean_player_data, columns=["Playlist_Id", "Embed_Html", "Playlist_Url"])
    clean_snippet_df = pd.DataFrame(data=clean_snippet_data, columns=["Playlist_Id", "Channel_Id", "Channel_Name", "Playlist_Published_At", "Playlist_Title", "Playlist_Description", "Playlist_Thumbnail_Default_Url"])

    temp_df = clean_content_details_df.merge(clean_player_df, on=["Playlist_Id"], how="inner")
    playlists_df = temp_df.merge(clean_snippet_df, on=["Playlist_Id"], how="inner")

    playlists_df.to_csv(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "csv", "playlists", "playlists.csv"), index=False)
    playlists_df.to_excel(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "xlsx", "playlists", "playlists.xlsx"), index=False)

def clean_search(channel_name, vid_ids, date):
    all_search = []
    for vid_id in vid_ids:
        clean_search_data = []
        with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "search", f"{vid_id}_search.json"), "r") as f:
            data = json.load(f)
            for item in data["items"]:
                clean_search_data.append([vid_id, item["id"]["videoId"], item["snippet"]["publishedAt"], item["snippet"]["channelId"], item["snippet"]["channelTitle"], item["snippet"]["title"], item["snippet"]["description"]])

            clean_search_df = pd.DataFrame(data=clean_search_data, columns=["Video_Id", "Related_Video_Id", "Related_Video_Published_At", "Related_Channel_Id", "Related_Channel_Name", "Related_Video_Title", "Related_Video_Description"])
            all_search.append(clean_search_df)

    super_df = all_search[0]
    del all_search[0]
    for curr_df in all_search:
        super_df = super_df.append(curr_df)

    super_df.to_csv(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "csv", "search", f"search.csv"), index=False)
    super_df.to_excel(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "xlsx", "search", f"search.xlsx"), index=False)

def clean_videos(channel_name, vid_ids, date):
    unordered_df_size = []
    for vid_id in vid_ids:
        clean_content_details_data = []
        clean_snippet_data = []
        clean_statistics_data = []

        with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "videos", f"{vid_id}_contentDetails_video.json"), "r") as f:
            data = json.load(f)
            clean_content_details_data.append([data["items"][0]["id"], data["items"][0]["contentDetails"]["duration"]])
            clean_content_details_df = pd.DataFrame(data=clean_content_details_data, columns=["Video_Id", "Video_Duration"])
   
        with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "videos", f"{vid_id}_snippet_video.json"), "r") as f:
            data = json.load(f)
            clean_snippet_data = [data["items"][0]["id"], data["items"][0]["snippet"]["publishedAt"], data["items"][0]["snippet"]["channelId"], data["items"][0]["snippet"]["channelTitle"], data["items"][0]["snippet"]["title"], data["items"][0]["snippet"]["description"], data["items"][0]["snippet"]["thumbnails"]["default"]["url"]]
            clean_snippet_df = pd.DataFrame(columns=["Video_Id", "Video_Published_At", "Channel_Id", "Channel_Name", "Video_Title", "Video_Description", "Thumbnails_Default_Url"])
            try:
                for i in range(len(data["items"][0]["snippet"]["tags"])):
                    clean_snippet_data.append(data["items"][0]["snippet"]["tags"][i])
                    clean_snippet_df[f"tag_{i+1}"] = "Null"
            except KeyError:
                pass
            clean_snippet_df.loc[len(clean_snippet_df)] = clean_snippet_data
    
        with open(os.path.join(os.getcwd(), f"{channel_name}_data", date, "raw", "videos", f"{vid_id}_statistics_video.json"), "r") as f:
            data = json.load(f)
            clean_statistics_data.append([data["items"][0]["id"], data["items"][0]["statistics"]["viewCount"], data["items"][0]["statistics"]["likeCount"], data["items"][0]["statistics"]["dislikeCount"], data["items"][0]["statistics"]["favoriteCount"], data["items"][0]["statistics"]["commentCount"]])
            clean_statistics_df = pd.DataFrame(data=clean_statistics_data, columns=["Video_Id", "View_Count", "Like_Count", "Dislike_Count", "Favorite_Count", "Comment_Count"])
    
        temp_df = clean_content_details_df.merge(clean_snippet_df, on=["Video_Id"], how="inner")
        video_df = temp_df.merge(clean_statistics_df, on=["Video_Id"], how="inner")
        
        unordered_df_size.append((-len(video_df.columns), video_df))

    ordered_df_size = sorted(unordered_df_size, key=lambda x:x[0])
    super_df = ordered_df_size[0][1]
    del ordered_df_size[0]
    for curr_df in ordered_df_size:
        super_df = super_df.append(curr_df[1])

    super_df.to_csv(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "csv", "videos", f"video.csv"), index=False, na_rep="Null")
    super_df.to_excel(os.path.join(os.getcwd(), f"{channel_name}_data", date, "clean", "xlsx", "videos", f"video.xlsx"), index=False, na_rep="Null")

if __name__ == "__main__":
    main()
