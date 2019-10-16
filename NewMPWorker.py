# coding=utf-8


from multiprocessing import Process, Lock

from CommonWorker import CommonWorker, common_run


class NewMPWorker(CommonWorker):
    def __init__(self, callback=None):
        super(NewMPWorker).__init__(callback)

    def start(self):
        self.task = Process(target=common_run, daemon=True)
        self.task.start()

    def stop(self):
        pass
