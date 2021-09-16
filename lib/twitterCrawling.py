import sys
sys.path.append("C:\\workspace\\news-alarm")
print(sys.path)

import twitter
from properties import commonProperties as config
import telegram
import time
from dateutil.parser import parse
from lib.logger import logger
import threading
import datetime as dt
import traceback


class twitterCrawling(object):
    def __init__(self,token,chat_id):
        self.token = token
        self.chat_id = chat_id

        self.twitter_api = twitter.Api(consumer_key=config.twitter_consumer_key,
                                consumer_secret=config.twitter_consumer_secret, 
                                access_token_key=config.twitter_access_token, 
                                access_token_secret=config.twitter_access_secret)
    def run(self):
        #@elonmusk
        #@cz_binance
        #@binance
        logger.debug("==================================================================")
        bot = telegram.Bot(token = self.token)

        # tmpCreatedAt = statuses[0].created_at
        index = 1
        pDateLIst = []

        currentTime = parse((dt.datetime.now()-dt.timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S")+"+00:00")
        while True:
            try:
                accounts = config.twitter_accounts
                for i in range(0, len(accounts)) :
                    
                    account = accounts[i]
                    statuses = self.twitter_api.GetUserTimeline(screen_name=account, count=5, include_rts=True, exclude_replies=False)
                    # logger.debug(statuses)
                    
                    for j in range(0, len(statuses)) :
                        
                        status = statuses[j]
                        createdAt = parse(status.created_at)
                        msg = "[twit_"+account+"] "+status.text
                        if(index == 1 and j == 0):
                            pDateLIst.insert(i,createdAt)


                        # logger.debug(currentTime)
                        # logger.debug(createdAt)
                        # logger.debug(pDateLIst[i])
                        if(createdAt < currentTime):
                            # logger.debug("continue")
                            continue

                        if(createdAt > pDateLIst[i]):
                            bot.sendMessage(chat_id = self.chat_id, text=msg, timeout=30)
                            logger.debug("########## : " + msg)
                            pDateLIst[i] = createdAt
                            logger.debug("[" + account + "]["+str(status.id)+"] currentTime["+str(i)+"] : " + str(currentTime))
                            logger.debug("[" + account + "]["+str(status.id)+"] pDateLIst["+str(i)+"] : " + str(pDateLIst[i]))
                            logger.debug("[" + account + "]["+str(status.id)+"] createdAt > currentTime : " + str(createdAt > pDateLIst[i]))

                    # logger.debug(status.text.encode('utf-8'))
                    time.sleep(5)
                time.sleep(30)
                index = index + 1
            except Exception as e:
                logger.error(account)
                logger.error(e)
                logger.error(traceback.format_exc())
                logger.debug("i : " + str(i))
                logger.debug("j : " + str(j))
                time.sleep(500)
                continue
        logger.debug("3 ==================================================================")
        output_file_name = "twitter_get_timeline_result.txt"
        with open(output_file_name, "w", encoding="utf-8") as output_file:
            for status in statuses:
                logger.debug(status, file=output_file)


# twitter_1 = twitterCrawling(config.twit_telgm_tokens, config.twit_chat_ids)
# t1 = threading.Thread(target=twitter_1.run, args=())
# t1.start()