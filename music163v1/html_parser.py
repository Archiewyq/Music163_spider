'''
Created on 2017年6月28日

@author: wyq
'''
from bs4 import BeautifulSoup
import urllib.parse


class HtmlParser(object):
    
    
    def get_new_urls(self, page_url, soup, x):
        new_urls = set()

#         links = soup.select("div#m-playlist div.g-sd4 div.g-wrap7 li div.cver a")
#         for link in links:
#             new_url = link.attrs['href']
#             new_full_url  = urllib.parse.urljoin(page_url, new_url)
# #             print(new_full_url)
#             new_urls.add(new_full_url)
        new_url = page_url[0:33]   
        new_url = new_url + str(x)   
        new_urls.add(new_url)
#         print(new_url)
        
        return new_urls
    
    
    def get_new_data(self, page_url, soup):
        res_data = []
        flag = 0
        
        list_pic = soup.select('div#m-playlist div.cover img')
        list_nameUrl = soup.select('div#m-playlist div.cnt div.tit h2')
        list_playcount = soup.select('div.u-title div.more strong#play-count')
        list_author = soup.select('div.m-info div.cnt div.cntc div.user span.name a.s-fc7')
        list_playlistcount = soup.select('span.sub span#playlist-track-count')
        list_allcount = soup.select('div#content-operation a')
        list_music = soup.select('div#song-list-pre-cache li a')

#         print(list_pic)
#         print(list_nameUrl)
#         print(list_playcount[0].text)
#         print(list_author)
#         print(list_playlistcount)
#         print(list_collectcount[2]['data-count'])
#         print(list_collectcount[3]['data-count'])
#         print(list_music)

        #无创建人、歌曲数、播放量的歌单不进行计算
        if len(list_author) != 0 and int(list_playlistcount[0].text) > 1: 
            if int(list_playcount[0].text) >= 100:
#                 print('歌单图片:'+list_pic[0]['data-src'])
#                 print('歌单名称:'+list_nameUrl[0].text)
#                 print('歌单ID:' +page_url.replace("http://music.163.com/playlist?",""))
#                 print('歌单播放量:'+list_playcount[0].text)
#                 print('歌单作者:'+list_author[0].text)
#                 print('作者ID:' +list_author[0]['href'])
#                 print('收藏数:'+list_collectcount)
                if list_allcount[2]['data-res-action'] == 'fav':
                    list_collectcount = list_allcount[2]['data-count']
#                     print('收藏数:'+list_collectcount[2]['data-count'])
                if list_allcount[3]['data-res-action'] == 'share':
                    list_sharecount = list_allcount[3]['data-count']
#                     print('分享数:'+list_collectcount[3]['data-count'])
                if list_allcount[5]['data-res-action'] == 'comment':
                    if list_allcount[5].next()[0].text != '评论':
                        list_commentcount = list_allcount[5].next()[0].text
                    else:
                        list_commentcount = 0
#                         print('评论数:'+list_collectcount[5].next()[0].text)
                #获取歌单中歌曲
                music = []
                for element in list_music:
#                     print(element['href'])
                    music.append([element.text, element['href']])
                
                flag = 1
                #歌单名、歌单ID、播放量、创建者、创建者ID、歌曲数、歌单封面、收藏数、分享数、评论数、歌曲列表
                res_data.append([ list_nameUrl[0].text, page_url, list_playcount[0].text, list_author[0].text, 
                                list_author[0]['href'], list_playlistcount[0].text, list_pic[0]['data-src'],
                                list_collectcount, list_sharecount, list_commentcount, music])     
        return res_data, flag
    
    
    def parse(self, page_url, html_cont, x):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, "lxml")
        new_urls =  self.get_new_urls(page_url, soup, x)
        new_data, flag = self.get_new_data(page_url, soup)
        return new_urls, new_data, flag
    
    



