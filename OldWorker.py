# coding=utf-8

from time import sleep
from threading import Thread, Lock
# from multiprocessing import Process, Lock
from random import randint


class OldWorker:
    def __init__(self, worker_id, msg_handler=None, callback=None):
        self.worker_id = worker_id
        self.msg_handler = msg_handler
        self.callback = callback
        self.task = None

    def start(self):
        self.task = Thread(target=self.run, daemon=True)
        # self.task = Process(target=self.run, daemon=True)
        self.task.start()

    def stop(self):
        pass

    def run(self):
        # Do nothing except waiting
        sec = randint(3, 10)
        self.call_msg_handler("[Task {}] Waiting {}s...".format(self.worker_id, sec))
        sleep(sec)
        self.call_msg_handler("[Task {}] Finished!".format(self.worker_id))

        # Call callback() after finished
        self.call_callback()
        self.call_msg_handler("[Task {}] Callback called!".format(self.worker_id))

    def join(self):
        if self.task:
            self.task.join()

    def call_msg_handler(self, msg):
        if self.msg_handler:
            self.msg_handler(msg)

    def call_callback(self):
        if self.callback:
            self.callback()
