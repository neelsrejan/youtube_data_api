from os import environ
from ytd_activities import Activities


def main():
    print(environ["YOUTUBE_DATA_API_KEY"])
    API_KEY = environ["YOUTUBE_DATA_API_KEY"]
    channel_id = "UCWPXl--e3JsJxRG64Of_msA"

    YT = Activities(API_KEY, channel_id)
    YT.list_content_details()
    #YT.json_stats()

if __name__ == "__main__":
    main()
