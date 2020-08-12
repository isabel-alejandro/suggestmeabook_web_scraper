import requests
from unidecode import unidecode

App_for_202 = "Final Project"


# When the function get_posts is called the subreddit r/suggestmeabook will be able to pass through and extract data from it.

def get_post_info(subreddit):
    """
    Returns data on top posts in r/suggestmeabook. Returns number of upvotes, titles of posts, and name.
    """

    # user-agent is set in order to receive data from the Reddit server.
    # rawdata is set to .json reddit data - I will be able to utilize the API view of Reddit data.

    url = f"https://www.reddit.com/r/{subreddit}.json?t=month&limit=100"
    head = {'user-agent': App_for_202}
    rawdata = requests.get(url, headers=head).json()

    # returndata is an empty list. when returndata is returned by my function, upvotes, title, username, name , and points will be appended to the empty thisitem dict.
    returndata = []

    listings = rawdata['data']['children']

    # thisitem is set to an empty  dictionary

    # thisitem is then appended to the empty list returndata
    for item in listings:
        thisitem = dict()
        thisitem['upvotes'] = int(item['data']['ups'])
        thisitem['title'] = unidecode(item['data']['title']).replace(",", " ").replace("\n", " ")
        thisitem['username'] = item['data']['name']
        thisitem['points'] = int(item['data']['score'])

        returndata.append(thisitem)

    return returndata


# contents of get_post_info is assigneed to the list 'data'
data = get_post_info("suggestmeabook")

targetsub = "suggestmeabook"

# print thisitem from dict.
print("What are the top posts right now in r/{targetsub}\n?")

for i in data:
    print(f"Redditor {i['username']} posted to r/{targetsub} and received {i['upvotes']} upvotes. This post has a total score of {i['points']} points. The title of this post is ' {i['title']}.\n")

# write raw data into a txt file
# with the txt file, I will be able to find the most common words used and load the data into an excel document.
with open('suggestmeabook.txt', 'w') as myfile:
    for post in data:
        line = f"{post['username']}, {post['upvotes']}, {post['points']}, {post['title']}\n"
        myfile.write(line)
