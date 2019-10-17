# coding=utf-8

from logging import getLogger, StreamHandler, Formatter, DEBUG

from OldWorker import OldWorker


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


class OldMainCls:
    def __init__(self, logger=None):
        self.logger = logger
        self.worker_id = 0
        self.worker_map = {}

    def gen_new_worker(self):
        def local_msg_handler(msg):
            self.logger.info(msg)

        def local_callback(wid=self.worker_id):
            self.worker_map.pop(wid)
            if self.logger:
                self.logger.info("<local_callback> len(worker_map)={}".format(len(self.worker_map)))

        self.worker_map[self.worker_id] = worker = OldWorker(self.worker_id,
                                                             msg_handler=local_msg_handler,
                                                             callback=local_callback)
        self.worker_id += 1
        if self.logger:
            self.logger.info("<gen_new_worker> len(worker_map)={}".format(len(self.worker_map)))
        return worker


if __name__ == "__main__":
    logger = get_logger()
    logger.info("In __main__ !")

    TASK_TYPE = "THREAD"
    N_TASKS = 10
    tasks = []
    main_cls = OldMainCls(logger=logger)

    logger.info("[{}] Pending {} tasks...".format(TASK_TYPE, N_TASKS))
    for i in range(N_TASKS):
        task = main_cls.gen_new_worker()
        tasks.append(task)
        task.start()
    logger.info("[{}] {} tasks prepared.".format(TASK_TYPE, N_TASKS))

    for i in tasks:
        i.join()
    logger.info("[{}] {} tasks all finished!".format(TASK_TYPE, N_TASKS))
