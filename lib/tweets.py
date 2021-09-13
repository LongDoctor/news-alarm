import GetOldTweets3 as got
import time
# 가져올 범위 정의
# 트럼프 임기 시작일: 2017년 1월 20일

import datetime    # datetime 패키지

days_range = []


# datetime 패키지, datetime 클래스(날짜와 시간 함께 저장)
# strptime 메서드: 문자열 반환
start = datetime.datetime.strptime("2017-01-20", "%Y-%m-%d")
end = datetime.datetime.strptime("2019-12-31", "%Y-%m-%d")

date_generated = [start+datetime.timedelta(days=x) for x in range(0, (end-start).days)]

for date in date_generated:
    days_range.append(date.strftime("%Y-%m-%d"))

print("===설정된 트윗 수집 기간: {} ~ {}===".format(days_range[0], days_range[-1]))
print("===총 {}일 간의 데이터 수집===".format(len(days_range)))


# tweetCriteria로 수집 기준 정의
tweetCriteria = got.manager.TweetCriteria().setUsername("realDonaldTrump").setSince("2017-01-20").setUntil("2019-12-31")


# 수집
print("데이터 수집 시작========")
start_time = time.time()

tweet = got.manager.TweetManager.getTweets(tweetCriteria)

print("데이터 수집 완료======== {0:0.2f}분".format((time.time() - start_time)/60))
print("=== 총 트윗 개수 {} ===".format(len(tweet)))