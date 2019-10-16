# coding=utf-8

from billiard import freeze_support

from logging import getLogger

if __name__ == "__main__":
    freeze_support()

    logger = getLogger()
    logger.info("In __main__ !")
