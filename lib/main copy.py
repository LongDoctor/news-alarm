import logging
import time
from datetime import datetime as date
logging.basicConfig(level=logging.DEBUG)

str1 = "2021-09-07 22:43:00+09:00"

logging.info(date.now())
logging.info(str(date.now())[11:13])
logging.info(int(str(date.now())[11:13]))

logging.info(str1)
logging.info(str1[11:13])
logging.info(int(str1[11:13]) >= 22 or int(str1[11:13]) <= 6)
