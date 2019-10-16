# coding=utf-8

from logging import getLogger

from OldWorker import OldWorker


class OldMainCls:
    def __init__(self, logger=None):
        self.logger = logger
        self.worker_id = 0
        self.worker_map = {}

    def gen_new_worker(self):
        def local_callback(wid=self.worker_id):
            self.worker_map.pop(wid)
            if self.logger:
                self.logger.info("<local_callback> worker_map={}".format(repr(self.worker_map)))

        self.worker_map[self.worker_id] = worker = OldWorker(callback=local_callback)
        self.worker_id += 1
        if self.logger:
            self.logger.info("<gen_new_worker> worker_map={}".format(repr(self.worker_map)))
        return worker


if __name__ == "__main__":
    logger = getLogger()
    logger.info("In __main__ !")

    main_cls = OldMainCls(logger=logger)
    tasks = []
    logger.info("Pending [Thread] tasks...")
    for i in range(10):
        tasks.append(main_cls.gen_new_worker())
    logger.info("[Thread] tasks prepared.")
    for i in tasks:
        i.join()
    logger.info("[Thread] tasks all finished!")
