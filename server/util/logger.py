import logging

def get_logger(logger_name, logger_path):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
    fh = logging.FileHandler(logger_path, encoding = 'utf-8')
    ch = logging.StreamHandler()
    fh.setLevel(logging.DEBUG)
    ch.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

if __name__ == '__main__':
    logger = get_logger('main', 'main.log')
    logger.info('TEST')