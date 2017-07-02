'''
Created on 2017年6月28日

@author: wyq
'''
# -*- coding: utf-8 -*-
import csv
import codecs
from filecmp import cmp
import time
from _elementtree import Element

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        
    
    def collect_data(self,data):
        if data is None:
            return 
        for element in data:
            self.datas.append(element)

    def sort_data(self):
        if self.datas is None:
            return
        for element in range(len(self.datas)):
#             if self.datas[element][2].find(r'万') != -1:
#                 end=  self.datas[element][2].find(r'万')
#                 self.datas[element][2] = int(self.datas[element][2][0:end])*10000
#             else:
            self.datas[element][2] = int(self.datas[element][2])
#         #从大到小排序        
        self.datas.sort(key=lambda x:x[2],reverse = True)  
          
    def output_html(self):
        self.sort_data()
        num = 0
        fout = open("output.html","w", encoding="utf-8")
        
        fout.write("<html>\n")
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'>\n</head>\n")
        fout.write("<body>\n")
        fout.write("<table boder='1 solid #CCC'>\n")

#         fout.write("<tr>\n")
        fout.write("<tr>\n<td align='center' colspan='13'><h3>获取时间：%s</h3></td>\n</tr>\n" %time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#         fout.write("<tr>\n")
        fout.write("<th>排名</th>")
        fout.write("<th>歌单名</th>")
        fout.write("<th>歌单ID</th>")
        fout.write("<th width='10'></th>")
        fout.write("<th>歌曲数</th>")
        fout.write("<th>播放量</th>")
        fout.write("<th>收藏数</th>")
        fout.write("<th>分享数</th>")
        fout.write("<th>评论数</th>")        
        fout.write("<th>创建人</th>")
        fout.write("<th>创建人ID</th>")
        fout.write("<th>歌单封面</th>")
        fout.write("<th>歌单列表</th>\n")
#         fout.write("</tr>\n")
        i = 0
        for data in self.datas:
            i = i+1
            fout.write("<tr align='center'>\n")
            #排名
            fout.write("<td align='center'>%d</td>\n" %i)
            #歌单名
            fout.write("<td align='left'><a href=%s>%s</a></td>\n"%(data[1], data[0]))
            #歌单ID
            fout.write("<td align='center'>%s</td>\n"%data[1].replace("http://music.163.com/playlist?id=",""))
            #空列
            fout.write("<td width='10'></td>")
            #歌曲数
            fout.write("<td align='center'>%s</td>\n"%data[5])
            #播放量
            fout.write("<td align='center'>%s</td>\n"%data[2])
            #收藏数
            fout.write("<td align='center'>%s</td>\n"%data[7])
            #分享数
            fout.write("<td align='center'>%s</td>\n"%data[8])
            #评论数
            fout.write("<td align='center'>%s</td>\n"%data[9])
            #创建人
            fout.write("<td align='center'><a href=%s>%s</a></td>\n"%("http://music.163.com"+data[4], data[3]))
            #创建人ID
            fout.write("<td align='center'>%s</td>\n"%data[4].replace("/playlist?id=","").replace("/user/home?id=",""))
            #歌单封面
            fout.write("<td align='center'><a href=%s>封面</a></td>\n" %data[6])
#             fout.write("<td align='center'>\n<a href=%s><img src=%s width='60' hight='60'></a>\n</td>\n" %("http://music.163.com"+data[1], data[6]))
            #歌单列表
#             print(data[10])
            fout.write("<td align='left'><font size='1'>\n")
            for element in data[10]:
#                 print(element)
                num += 1
                fout.write("<a href=%s>%s</a>\n" %('http://music.163.com'+element[1], element[0]))
            fout.write("</font></td>\n")
            
            fout.write("</tr>\n")
        
        fout.write("</table>\n")
        fout.write("</body>\n")
        fout.write("</html>\n")
        
        fout.close()
        print("歌曲总数:%d" %num)

    
    def output_excel(self):

        with codecs.open("test1.csv", "w+", "utf_8_sig") as csvfile:
            cfile = csv.writer(csvfile, dialect="excel")
            cfile.writerow(['歌单名','歌单ID','播放量','创建人','创建人ID','歌单封面'])
            for data in self.datas:
                cfile.writerow([data[0], data[1].replace("/playlist?id=",""), data[2], data[3], 
                                data[4].replace("/playlist?id=","").replace("/user/home?id=",""), 
                                data[5], data[6], data[7]])
            
    
    
    
    
    



