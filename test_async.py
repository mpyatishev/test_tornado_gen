import gc
import tornado
from tornado import gen
import time

import testing
testing.reps = 100000
testing.replist = range(testing.reps)


def get_data(callback=None):
    tornado.ioloop.IOLoop().add_timeout(time.time(), callback)


@gen.engine
def test_engine(callback=None):
    yield gen.Task(get_data)


@gen.coroutine
def test_coroutine(callback=None):
    yield gen.Task(get_data)


def test_raw(callback=None):
    def done():
        pass
    get_data(done)


def run(func):
    mem = testing.memory()
    elapsed, res = testing.timer(func)
    print('%--9s: %.5f, memory used = %.5f' % (func.__name__, elapsed,
                                               testing.memory() - mem))


def run_test_raw():
    run(test_raw)


def run_test_engine():
    run(test_engine)


def run_test_coroutine():
    run(test_coroutine)


if __name__ == '__main__':
    for func in (run_test_raw, run_test_engine, run_test_coroutine):
        gc.collect()
        ioloop = tornado.ioloop.IOLoop()
        ioloop.run_sync(func)
