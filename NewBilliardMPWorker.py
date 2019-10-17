# coding=utf-8


from billiard import Process, Lock
from logging import getLogger

from CommonWorker import CommonWorker, common_run


class NewBilliardMPWorker(CommonWorker):
    def __init__(self, callback=None):
        super(NewBilliardMPWorker).__init__(callback)

    def start(self):
        self.task = Process(target=common_run, daemon=True)
        self.task.start()

    def stop(self):
        pass
