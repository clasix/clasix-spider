#! /usr/bin/env python
#coding=utf-8

import requests
from os.path import dirname, abspath
from extract import extract, extract_all
import re
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
RE_CN = re.compile(ur'[\u4e00-\u9fa5]+')
PREFIX = dirname(abspath(__file__))


with open("%s/highschool.sh"%PREFIX, "w") as down:
    r = requests.get('http://s.xnimg.cn/js/cityArray.js')
    if r.status_code == 200:
        for json_str in extract_all('=', ";", r.content):
            json_obj = json.loads(json_str)
            for area in json_obj:
                [num, name] = area.split(':')
                res = requests.get('http://support.renren.com/highschool/%s.html'%num)
                if res.status_code == 200:
                    print num, name
                    down.write('wget http://support.renren.com/highschool/%s.html -O %s/highschool/%s%s.html\n'%(num, PREFIX, name, num))
        for json_str in extract_all(' "', '\n', r.content):
            for entry in json_str.split('","'):
                [num, name] = entry.split(':')
                name = name.replace('"', '')
                res = requests.get('http://support.renren.com/highschool/%s.html'%num)
                print num, name
                if res.status_code == 200:
                    print num, name
                    down.write('wget http://support.renren.com/highschool/%s.html -O %s/highschool/%s%s.html\n'%(num, PREFIX, name, num))
        
