import sys
sys.path.append("d:\\999_python\\news_alarm")
print(sys.path)

import twitter
from properties import commonProperties as common
import telegram
import time

twitter_api = twitter.Api(consumer_key=common.twitter_consumer_key,
                          consumer_secret=common.twitter_consumer_secret, 
                          access_token_key=common.twitter_access_token, 
                          access_token_secret=common.twitter_access_secret)


account = "@cz_binance"
#@elonmusk
#@cz_binance
#@binance
statuses = twitter_api.GetUserTimeline(screen_name=account, count=10, include_rts=True, exclude_replies=False)
print("1 ==================================================================")
print(statuses)

keywords = common.keywords
token = common.telgm_tokens
chat_id = common.chat_ids
sortType = common.sortTypes
print("2 ==================================================================")
tmpCreatedAt = statuses[0].created_at
index = 1
i = 0
bot = telegram.Bot(token = token)
while True:
    for status in statuses:
        createdAt = status.created_at
        msg = status.text
        if(index == 1):
            if(i==0):
                tmpCreatedAt = status.created_at
            # bot.sendMessage(chat_id = chat_id, text=msg, timeout=30)
            i=i+1
        elif(status.created_at > tmpCreatedAt):
            # bot.sendMessage(chat_id = chat_id, text=msg, timeout=30)
            tmpCreatedAt = status.created_at

        print("["+str(i)+"]"+status.text)
        print(status.created_at +","+ tmpCreatedAt)
        print(status.created_at > tmpCreatedAt)
        tmpCreatedAt = status.created_at
        # print(status.text.encode('utf-8'))
    time.sleep(5)
print("3 ==================================================================")
output_file_name = "twitter_get_timeline_result.txt"
with open(output_file_name, "w", encoding="utf-8") as output_file:
    for status in statuses:
        print(status, file=output_file)