'''
Created on 2017年6月28日

@author: wyq
'''
# -*- coding: utf-8 -*-
import urllib.request
import urllib

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        })
        
        response = urllib.request.urlopen(req)
        content = response.read().decode('utf-8')

        if response.getcode() != 200:
            return None
        return content

