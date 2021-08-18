from os import environ
from ytd_activities import Activities
from ytd_captions import Captions


def main():
    API_KEY = environ["YOUTUBE_DATA_API_KEY"]
    channel_id = input("Welcome to the Youtube Data API page \nWhat is the ID of the channel you wish to get information about? ")
    YT = Activities(API_KEY, channel_id)
    YT.get_total_activities()
    print(f"The total activity of the channel is {YT.tot_activity}")
    numResults = YT.ask_for_num_activities()
    YT.ask_for_which_activity(numResults)
    

if __name__ == "__main__":
    main()
