#/usr/bin/env python3
import multiprocessing as mp
from termcolor import colored
import time
import os

city_list = []
index = 1
with open('./city.txt', 'rt') as f:
    for city in f:
        city_list.append(city.strip())


def test_one(city: str):
    os.system('./test_ {0}'.format(city))


def test_one_callbak(result):
    global index
    print(colored('{} finished'.format(index), 'red'))
    index += 1


if __name__ == '__main__':
    mp.set_start_method('fork')
    with mp.Pool() as pool:
        pool.map(test_one, city_list)
        pool.terminate()
