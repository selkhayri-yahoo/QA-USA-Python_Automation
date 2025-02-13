import logging   # import logging library

def get_logger(name, level=logging.INFO):
    # create logger with 'spam_application'
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # create file handler which logs even debug messages
    fh = logging.FileHandler('routes.log')
    fh.setLevel(level)
    logger.addHandler(fh)

    return logger
