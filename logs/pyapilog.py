# -*-coding:utf-8 -*-
# !/usr/bin/python

import logging, datetime, os, setting
logLevel = {
    1 : logging.NOTSET,
    2 : logging.DEBUG,
    3 : logging.INFO,
    4 : logging.WARNING,
    5 : logging.ERROR,
    6 : logging.CRITICAL
}
setFile = os.path.join(setting.root_dir,'setting.ini')
loggers = {}
def pyapilog(**kwargs):
    global loggers
    log_level = setting.logLevel
    log_path = setting.logFile
    if os.path.exists(log_path):
        log_file = os.path.join(log_path, datetime.datetime.now().strftime('%Y-%m-%d') + '.log')
    else:
        os.mkdir(r'%s' % log_path)
        log_file = os.path.join(log_path, datetime.datetime.now().strftime('%Y-%m-%d') + '.log')
    logger = logging.getLogger()
    logger.setLevel(logLevel[log_level])
    if not logger.handlers:
        fh = logging.FileHandler(log_file)
        fh.setLevel(logLevel[log_level])
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        loggers.update(dict(name=logger))
    return logger

