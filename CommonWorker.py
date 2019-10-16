# coding=utf-8


from time import sleep
from logging import getLogger


def common_run(worker_id):
    logger = getLogger()

    # Do nothing except waiting
    logger.info("[Task {}] Waiting...".format(self.worker_id))
    sleep(10)
    logger.info("[Task {}] Finished!".format(self.worker_id))

    # Call callback() after finished
    if callback:
        callback()
        logger.info("[Task {}] Callback called!".format(self.worker_id))

    # TODO Call callback() after finished


class CommonWorker:
    def __init__(self, callback=None):
        self.logger = getLogger()
        self.callback = callback
        self.task = None

    def start(self):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()
