import sys
sys.path.append("d:\\999_python\\news_alarm")
print(sys.path)

import twitter
from properties import commonProperties as config

twitter_api = twitter.Api(consumer_key=config.twitter_consumer_key,
                          consumer_secret=config.twitter_consumer_secret, 
                          access_token_key=config.twitter_access_token, 
                          access_token_secret=config.twitter_access_secret)


account = "@cz_binance"
#@elonmusk
#@cz_binance
#@binance
statuses = twitter_api.GetUserTimeline(screen_name=account, count=10, include_rts=True, exclude_replies=False)
print("1 ==================================================================")
print(statuses)


print("2 ==================================================================")
tmp = statuses[0].created_at
for status in statuses:
    print(status.text)
    # print(status.created_at +","+ tmp)
    # print(status.created_at < tmp)
    # tmp = status.created_at
    # print(status.text.encode('utf-8'))

print("3 ==================================================================")
output_file_name = "twitter_get_timeline_result.txt"
with open(output_file_name, "w", encoding="utf-8") as output_file:
    for status in statuses:
        print(status, file=output_file)