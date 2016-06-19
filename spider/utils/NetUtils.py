# -*- coding: utf-8 -*-
__author__ = 'zhuqi259'

import urllib.request
from nets.Proxy import get_proxy_from_cnproxy
from nets.UserAgent import get_user_agent
from utils.FileUtils import exists


def url_open(url, proxy_in_use=False, ua_in_use=True):
    if proxy_in_use:
        # proxy
        proxy = get_proxy_from_cnproxy()
        ip, port = proxy
        proxy_support = urllib.request.ProxyHandler({'http': "{0}:{1}".format(ip, port)})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)

    req = urllib.request.Request(url)

    if ua_in_use:
        # header
        user_agent = get_user_agent()
        req.add_header("User-Agent", user_agent)

    response = urllib.request.urlopen(req)
    return response.read()


def save_img(pic_url, save_path):
    if not exists(save_path):
        pic = url_open(pic_url)
        with open(save_path, "wb") as f:
            f.write(pic)
