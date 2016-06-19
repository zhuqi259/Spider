# -*- coding: utf-8 -*-
__author__ = 'zhuqi259'

from nets.Proxy import get_proxy_from_cnproxy

if __name__ == '__main__':
    proxy = get_proxy_from_cnproxy()
    ip, port = proxy
    print("{0}:{1}".format(ip, port))
