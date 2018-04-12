import inspect
import logging


def customLogger(logLevel):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(
        "{0}.log".format(loggerName), mode='w')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter(
        'format=%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%m/%d/%Y %H:%M:%S')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger