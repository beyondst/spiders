#/usr/bin/env python
# -*- coding=utf-8 -*-

import urllib
import urllib2
import re
import os

def post(url, data, key):
    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    #enable cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)
    # visit Game of Thrones webpage with cookie
    yyets = opener.open('http://www.yyets.com/resource/a10733')
    respHtml = yyets.read()
    find = re.search(key, respHtml)
    if find:
        os.system('echo "Winter is coming"|mutt @')

def main():
    posturl = "http://www.yyets.com/User/Login/ajaxLogin"
    data = {'account':'nickname',
            'password':'pwd',
            'from':'loginpage',
            'remember':'0',
            'url_back':''} 
    key = "S04E03.中英字幕"      
    post(posturl, data, key)
if __name__ == '__main__':
    main()
