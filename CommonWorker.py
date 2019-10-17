# coding=utf-8


from time import sleep
from logging import getLogger, StreamHandler, Formatter, DEBUG
from random import randint


def get_logger():
    logger = getLogger()
    if len(logger.handlers) <= 0:
        stream_handler = StreamHandler()
        stream_handler.setLevel(DEBUG)

        datefmt_str = '%Y-%m-%d %H:%M:%S'
        format_simple_str = '[%(asctime)s][%(levelname)s]%(message)s'
        formatter_simple = Formatter(format_simple_str, datefmt_str)
        stream_handler.setFormatter(formatter_simple)

        logger.addHandler(stream_handler)
        logger.setLevel(DEBUG)
    return logger


def common_run(worker_id):
    logger = get_logger()

    # Do nothing except waiting
    sec = randint(3, 10)
    logger.info("[Task {}] Waiting {}s...".format(worker_id, sec))
    sleep(randint(3, 10))
    logger.info("[Task {}] Finished!".format(worker_id))

    # Call callback() after finished
    if callback:
        callback()
        logger.info("[Task {}] Callback called!".format(worker_id))

    # TODO Call callback() after finished


class CommonWorker:
    def __init__(self, msg_handler=None, callback=None):
        self.msg_handler = callback
        self.callback = callback
        self.task = None

    def start(self):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()

    def call_msg_handler(self, msg):
        if self.msg_handler:
            self.msg_handler(msg)

    def call_callback(self):
        if self.callback:
            self.callback()
