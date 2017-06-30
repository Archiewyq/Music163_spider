'''
Created on 2017年6月28日

@author: wyq
'''
from bs4 import BeautifulSoup
import re
import urllib.parse


class HtmlParser(object):
    
    
    def get_new_urls(self, page_url, soup):
        new_urls = set()

        links = soup.select("div.u-page a.znxt")
#         print("lens of links: %d" %len(links))
        for link in links:
            new_url = link["href"]
            if new_url != "javascript:void(0)":
                new_full_url  = urllib.parse.urljoin(page_url, new_url)
                print(new_full_url)
                new_urls.add(new_full_url)
        
        return new_urls
    
    
    def get_new_data(self, page_url, soup, x):
        res_data = []
        y = 1
        list_pic = soup.select('ul#m-pl-container li div img')
        list_nameUrl = soup.select('ul#m-pl-container li div a.msk')
        list_num = soup.select('div.bottom span.nb')
        list_author = soup.select('ul#m-pl-container li p a.nm')
        n = 0
        length = len(list_pic)
        while n < length:
#             print('歌单图片:'+list_pic[n]['src'])
#             print('歌单名称:'+list_nameUrl[n]['title'])
#             print('歌单ID:' +list_nameUrl[n]['href'].replace("/playlist?",""))
#             print('歌单播放量:'+list_num[n].text)
#             print('歌单作者:'+list_author[n]['title'])
#             print('作者ID:' +list_author[n]['href'].replace("/playlist?","").replace("/user/home?","")+'\n')
            res_data.append([list_nameUrl[n]['title'], list_nameUrl[n]['href'],  
                            list_num[n].text, list_author[n]['title'], list_author[n]['href'],
                            list_pic[n]['src'], x, y ])
            y += 1
            n += 1     
        return res_data
    
    
    def parse(self, page_url, html_cont, x):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, "lxml")
        new_urls =  self.get_new_urls(page_url, soup)
        new_data = self.get_new_data(page_url, soup, x)
        return new_urls, new_data
    
    



