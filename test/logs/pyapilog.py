# coding=utf-8
import logging, datetime, os, setting
logLevel = {
    1 : logging.NOTSET,
    2 : logging.DEBUG,
    3 : logging.INFO,
    4 : logging.WARNING,
    5 : logging.ERROR,
    6 : logging.CRITICAL
}
setFile = os.path.join(setting.root_dir,'setting.py')

"""
定义日志方法，从配置文件读取日志等级，且定义日志输出路径
"""
def pyapilog(**kwargs):
    global  loggers
    log_level = setting.logLevel
    log_path = setting.logFile
    if os.path.exists(log_path):
        log_file = os.path.join(log_path,datetime.datetime.now().strftime('%y-%m-%d')+'.log')
    else:
        os.mkdir(r'%s' % log_path)
        log_file = os.path.join(log_path,datetime.datetime.now().strftime('%y-%m-%d')+'.log')
    logger = logging.getLogger()
    logger.setLevel(logLevel[log_level])
    if not logger.handlers:
        '''创建一个handler，用于写入日志文件'''
        fh = logging.FileHandler(log_file)
        fh.setLevel(logLevel[log_level])
        '''再创建一个handler，用于输出到控制台'''
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        '''定义handler输出格式'''
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        '''给logger添加handler'''
        logger.addHandler(fh)
        logger.addHandler(ch)
        '''将装载了log的字典存入全局变量loggers中'''
        loggers.update(dict(name=logger))
        return logger
