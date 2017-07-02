'''
Created on 2017骞�6鏈�28鏃�

@author: wyq
'''
# -*- coding: utf-8 -*-
from music163_spider import  html_downloader, html_parser, html_outputer,\
    url_manager


class SpiderMain(object):
    
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 0
        x = 999992
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try :
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url)
                new_urls, new_data, flag= self.parser.parse(new_url, html_cont, x)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                x = x+1

                if count == 500:
                    break
                if flag == 1:
                    print('craw %d:%s' % (count, new_url))
                    count = count + 1
            except Exception as e:
                self.outputer.output_html()
                print('craw failed',e)
                 

        self.outputer.output_html()                 #杈撳嚭缃戦〉鏂囦欢
#         self.outputer.output_excel()                #杈撳嚭excel鏍煎紡
        print("Work Done!")

if __name__ == "__main__":
    root_url = "http://music.163.com/playlist?id=1"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)