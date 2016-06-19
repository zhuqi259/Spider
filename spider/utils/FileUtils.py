# -*- coding: utf-8 -*-
__author__ = 'zhuqi259'

"""
文件操作工具类
"""
import pickle
import os.path


def read_data(filename):
    with open(filename, 'rb') as f:
        return f.read()


def save_pickle(data, pkl):
    with open(pkl, 'wb') as f:
        pickle.dump(data, f)


def load_pickle(pkl):
    with open(pkl, 'rb') as f:
        return pickle.load(f)


def exists(filename):
    return os.path.exists(filename)
