# -*- coding: utf-8 -*-
__author__ = 'zhuqi259'

"""
Dependencies:
 * beautifulsoup4
"""
from bs4 import BeautifulSoup
import random
import os


def get_html_data(filename):
    with open(filename, 'rb') as f:
        return f.read()


def get_proxy_from_cnproxy(filename):
    html_doc = get_html_data(filename).decode('utf-8')
    soup = BeautifulSoup(html_doc, 'html.parser')
    tbodys = soup.find_all("tbody")
    proxies = []
    for tbody in tbodys:
        trs = tbody.find_all("tr")
        for tr in trs:
            tds = tr.find_all('td')
            if tds:
                ip = tds[0].string
                port = tds[1].string
                proxies.append((ip, port))
    return random.choice(proxies)


if __name__ == "__main__":
    proxy_filename = os.path.join(os.path.pardir, "data/cn-proxy.com.html")
    proxy = get_proxy_from_cnproxy(proxy_filename)
    ip, port = proxy
    print("{0}:{1}".format(ip, port))
