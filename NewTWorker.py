# coding=utf-8


from threading import Thread, Lock
from logging import getLogger

from CommonWorker import CommonWorker, common_run


class NewTWorker(CommonWorker):
    def __init__(self, callback=None):
        super(NewTWorker).__init__(callback)

    def start(self):
        self.task = Thread(target=self.run, daemon=True)
        self.task.start()

    def stop(self):
        pass
