import os
import logging
from logging.handlers import TimedRotatingFileHandler


log_dir = './logs'

if not os.path.exists(log_dir):
    os.mkdir(log_dir)

logger = logging.getLogger(__name__)
formatter = logging.Formatter(u'%(asctime)s [%(levelname)8s] %(message)s')
logger.setLevel(logging.DEBUG)


fileHandler = TimedRotatingFileHandler(filename='./logs/py_sched.log', when='midnight', interval=1, encoding='utf-8')
fileHandler.setFormatter(formatter)
fileHandler.suffix = '%Y%m%d'
fileHandler.setLevel(logging.DEBUG)
logger.addHandler(fileHandler)

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
streamHandler.setLevel(logging.DEBUG)
logger.addHandler(streamHandler)

