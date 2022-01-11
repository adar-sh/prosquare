

import time
import tweepy



consumer_key=''

consumer_secret=''

access_token=''

access_token_secret=''


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)


mentions = api.mentions_timeline(count=1)

while True:
    for mention in mentions:
        thread_id=mention.in_reply_to_status_id
        mentioner=mention.user.screen_name
    user=api.get_user(mentioner)
    mentioner_id=user.id_str

    dm_data=api.get_status(thread_id)
    thread=dm_data.text

    idlist=open("idfile.txt","r")
    idlist=idlist.readlines()
    
    if str(thread_id)+"\n" not in idlist:
        try:
            direct_message = api.send_direct_message(mentioner_id,thread)
            print(direct_message.message_create["message_data"]["text"])
            idwritelist = open("idfile.txt","a")
            idwritelist.write(str(thread_id)+"\n")
        except:
            print("you cannot message this user")
    else:
        print("already sent")
    time.sleep(600)
