

import tweepy



consumer_key='zJkas3FrAWaKR85xDkzIc5BoD'

consumer_secret='7Y595SHWNTrDkLNZFpj8unG7QVEOrTIj7ilKn4Cd2eXhZ6A5tl'

access_token='1390673212212613127-wuWEc5GEg3zlTzbMWQ5T4OTBjXNWYX'

access_token_secret='VfKfhtx20hYhv96VEDN3jkCNk3lFGeGAPrdrCjHdC3New'


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)


mentions = api.mentions_timeline(count=1)

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
        idlist = open("idfile.txt","a")
        idlist.write(str(thread_id)+"\n")
    except:
        print("you cannot message this user")
else:
    print("already sent")

