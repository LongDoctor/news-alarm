import logging
import sys

from telegram import chat
sys.path.append("d:\\999_python\\news_alarm")
print(sys.path)

import requests
from requests.adapters import HTTPAdapter
import time
import datetime
from datetime import datetime as date
from dateutil.parser import parse
import telegram
import threading
from properties import commonProperties as common
from lib.logger import logger

# 패치
# 야간모드
# 최초 알림 시점, 현재시간보다 1일 전 데이터는 제외
# 명령어 받기
# 키워드 갯수에 맞게 쓰레드 분기처리(1 : 5)
# 서버재시작시 이전기사 보내기 말기
# 트위터 크롤링

# 에러
# 키워드별 쓰레드가 아닌 한 쓰레드(유저기준)에서 키워드가 루프돌도록
# 'telegram.error.RetryAfter vlog.io/@gyunghoe/텔레그램-봇-성능-최적화하기

def test(s):
    logger.debug(s)

def print_api_respones(log):
    logger.debug(log)
    logger.debug()

def sned_telegram_msg(bot, chat_id, msg):
    bot = telegram.Bot(token = token)
    bot.sendMessage(chat_id = chat_id, text=msg, timeout=30)

# def run(keyword, chat_id, token, sortType):
def run(keyword, chat_id, token, sortType):
    start_time = time.time()

    #Naver API Params
    index = 1 #처음 LOOP의 마지막 뉴스기사의 시간을 가져오기 위한 INDEX
    cnt = 0
    
    #단일건로직
    pDateLIst = []

    while True:
        # for keyword in keywords:
        try:
            for k in range(0, len(keywords)) :
                keyword = keywords[k]
                params = {"query":keyword, "display":common.displayNum, "start":common.startNum, "sort":sortType}
                sess = requests.Session()
                adapter = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
                sess.mount('https://', adapter)
                r = sess.get(common.url, params= params, headers = common.headers)
                j = r.json()
                # current_HH = int(str(date.now())[11:13])
                logger.debug("*************************************************************************")
                # print_api_respones(j)

                bot = telegram.Bot(token = token)
                # updates = bot.getUpdates()

                #텔레그램 메세지 명령어 받기
                # for u in updates :
                #     data = u.channel_post
                #     if  data["text"]:
                #         print(0)

                # logger.info("k"+str(k)+" key "+keyword)
               
                for i in range(0, len(j["items"])) :

                    item = j["items"][i]
                    parsePDate = parse(item["pubDate"])
                    msg = item["title"]+"\n "+item["link"]

                #   if(common.night_mode and (current_HH > 22 or current_HH < 7)):
                #       continue

                    if(index == 1):

                        if(i == common.startNum-1):
                            # tempTime = parsePDate
                            logger.info("k " + str(k) + " i " +str(i) +" "+ keyword)
                            pDateLIst.insert(k,parsePDate) #단일건
                    
                        sned_telegram_msg(bot,chat_id,msg)
                        cnt = cnt + 1
                    elif(parsePDate > pDateLIst[k]):

                        sned_telegram_msg(bot,chat_id,msg)
                        # tempTime = parsePDate 
                        pDateLIst[k] = parsePDate #단일건
                        cnt = cnt + 1
                    
                logger.debug("index : {} ,keyword : {}, news : {}".format(index, keyword, cnt) +", 실행 시간 : "+str(datetime.timedelta(seconds=time.time()-start_time)).split(".")[0])
                logger.debug("pDataList["+str(k)+"] : "+str(pDateLIst[k]))
                # logger.debug("현재 뉴스 시간 : " + str(parsePDate))
                # logger.debug("마지막 기사 시간 : " + str(tempTime))
                time.sleep(common.thread_sleep_time)

        except Exception as e:

            logger.error(sys.exc_info()[0])
            logger.error(e)
            logger.error(token)
            logger.error(chat_id)
            logger.error(keyword)
            sned_telegram_msg(token,chat_id,"ERROR_"+keyword+"._."+chat_id)
            time.sleep(10)
            continue

        finally :
            sess.close()

                
            index = index + 1

keywords = common.keywords
token = common.telgm_tokens
chat_id = common.chat_ids
sortType = common.sortTypes
run(keywords,chat_id,token,sortType)

# for  i in range(0,len(common.telgm_nms)):

#     chat_id = common.chat_ids[i]
#     token = common.telgm_tokens[i]
#     keywords = common.keywords[i]
#     sortType = common.sortTypes[i]
#     time.sleep(1)

#     for keyword in keywords :
#         if(i%4 == 0):
#             t4 = threading.Thread(target=run, args=(keyword, chat_id, token, sortType))
#             t4.start()
#         elif(i%3 == 0):
#             t3 = threading.Thread(target=run, args=(keyword, chat_id, token, sortType))
#             t3.start()
#         elif(i%2 == 0):
#             t2 = threading.Thread(target=run, args=(keyword, chat_id, token, sortType))
#             t2.start()
#         else:
#             t1 = threading.Thread(target=run, args=(keyword, chat_id, token, sortType))
#             t1.start()
#         time.sleep(10)