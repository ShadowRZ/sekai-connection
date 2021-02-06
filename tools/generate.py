#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import sys

TEMPLATE = """\
# 你的显示名
name: {}
# 你的用户名（ASCII Only 时）
nick: {}
# 你的网站或博客
site: {}
# 你的博客友链，是个列表，列表里面是友链对象的网站
links:
  # 像这样一行一项
"""

def main(name, nick, site):
    print(TEMPLATE.format(name, nick, site))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
