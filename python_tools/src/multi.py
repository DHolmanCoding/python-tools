import os
from multiprocessing.pool import ThreadPool
from multiprocessing.pool import Pool as ProcessPool
from enum import Enum


class MultiType(Enum):
    threading = ThreadPool
    processing = ProcessPool


def multiplex(function, data, multi_type: MultiType):
    num_cpus = os.cpu_count()

    with multi_type.value(processes=num_cpus) as multiplex_pool:
        return filter(None, multiplex_pool.map(function, data))


if __name__ == "__main__":
    x = MultiType.processing
    print(x.value)
