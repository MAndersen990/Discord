import praw
import random
import json
import project_ids



def pics(name):
    reddit = praw.Reddit(client_id= project_ids.client_id(),
                         client_secret=project_ids.secret_id(),
                         user_agent='/u/ Lightnin_Ahishatsu discord bot imgur getter')
    list = []

    for anotherone in reddit.subreddit(name).hot():
        if "imgur" in anotherone.url:
                list.append(anotherone.url)
        else:
            continue
    random.shuffle(list)
    z = random.randint(0,len(list)-1)
    return list[z]

def gifs(name):
    reddit = praw.Reddit(client_id=project_ids.client_id(),
                         client_secret=project_ids.secret_id(),
                         user_agent='/u/ Lightnin_Ahishatsu discord bot gif getter')
    list = []
    for theone in reddit.subreddit(name).hot():
        if "gfycat" in theone.url:
            list.append(theone.url)
        else:
            continue
    random.shuffle(list)
    z = random.randint(0, len(list) - 1)
    return list[z]

