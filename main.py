from os import environ
from ytd_activities import Activities


def main():
    API_KEY = environ["YOUTUBE_DATA_API_KEY"]
    channel_id = input("Welcome to the Youtube Data API page \nWhat is the ID of the channel you wish to get information about? ")
    YT = Activities(API_KEY, channel_id)
    YT.get_total_activities()
    print(f"The total activity of the channel is {YT.tot_activity}")
    numResults = YT.ask_for_num_activities()
    YT.ask_for_which_activity(numResults)

'''
def ask_for_which_activity(YT, numResults):
    which_activity = input("Which activity do you want to see for the channel? \nType c for content details, i for id, and s for snippet ")[0].lower()
    if which_activity == 'c':
        YT.list_content_details(numResults)
    elif which_activity == 'i':
        YT.list_id(numResults)
    elif which_activity == 's':
        YT.list_snippet(numResults)
    else:
        print("Invalid response, please enter a valid letter")
        ask_for_which_activity(numResults)

def ask_for_num_activity(maxVal):
    userVal = int(input(f"Choose how many activites you wish to see upto {maxVal} "))
    if userVal <= maxVal:
        return userVal
    else:
        print("Invalid response, please enter another number")
        ask_for_activity(maxVal)
'''
if __name__ == "__main__":
    main()
