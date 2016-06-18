# -*- coding: utf-8 -*-
__author__ = 'zhuqi259'

from proxy.GetProxy import get_proxy_from_cnproxy
import os


if __name__ == '__main__':
    proxy_filename = os.path.join(os.path.pardir, "data/cn-proxy.com.html")
    proxy = get_proxy_from_cnproxy(proxy_filename)
    ip, port = proxy
    print("{0}:{1}".format(ip, port))
