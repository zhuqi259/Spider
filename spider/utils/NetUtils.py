# -*- coding: utf-8 -*-
__author__ = 'zhuqi259'

import urllib.request
from urllib.error import URLError, HTTPError
from nets.Proxy import get_proxy_from_cnproxy
from nets.UserAgent import get_user_agent
from utils.FileUtils import exists
import time


def url_open(url, timeout, count, proxy_in_use=False, ua_in_use=True):
    def real_url_open():
        time.sleep(0.5)
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

        try:
            response = urllib.request.urlopen(req, timeout=timeout)
            return True, response.read()
        except HTTPError as e:
            print('Error code:', e.code)
            return False, bytes()
        except URLError as e:
            print('Reason', e.reason)
            return False, bytes()
        except Exception as e:
            print(e)
            return False, bytes()

    index = 0
    while index < count:
        flag, content = real_url_open()
        if flag:
            return flag, content
    return False, bytes()


def save_img(pic_url, save_path):
    if not exists(save_path):
        flag, pic = url_open(pic_url, timeout=60)
        if flag:
            with open(save_path, "wb") as f:
                f.write(pic)
