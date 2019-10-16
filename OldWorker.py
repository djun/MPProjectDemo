# coding=utf-8

from time import sleep
from threading import Thread, Lock
from logging import getLogger


class OldWorker:
    def __init__(self, worker_id, logger=None, callback=None):
        self.worker_id = worker_id
        self.logger = logger or getLogger()
        self.callback = callback
        self.task = None

    def start(self):
        self.task = Thread(target=self.run, daemon=True)
        self.task.start()

    def stop(self):
        pass

    def run(self):
        # Do nothing except waiting
        self.logger.info("[Task {}] Waiting...".format(self.worker_id))
        sleep(10)
        self.logger.info("[Task {}] Finished!".format(self.worker_id))

        # Call callback() after finished
        if self.callback:
            self.callback()
            self.logger.info("[Task {}] Callback called!".format(self.worker_id))
