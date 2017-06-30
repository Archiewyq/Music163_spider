'''
Created on 2017年6月28日

@author: wyq
'''
# -*- coding: utf-8 -*-
import csv
import codecs
from filecmp import cmp

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
            if self.datas[element][2].find(r'万') != -1:
                end=  self.datas[element][2].find(r'万')
                self.datas[element][2] = int(self.datas[element][2][0:end])*10000
            else:
                self.datas[element][2] = int(self.datas[element][2])
        #从大到小排序        
        self.datas.sort(key=lambda x:x[2],reverse = True)  
          
    def output_html(self):
        self.sort_data()
        fout = open("output.html","w", encoding="utf-8")
        
        fout.write("<html>\n")
        fout.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'>\n</head>\n")
        fout.write("<body>\n")
        fout.write("<table boder='1' >\n")

        fout.write("<tr>\n")
        fout.write("<th>排名</th>\n")
        fout.write("<th>歌单名</th>\n")
        fout.write("<th>歌单ID</th>\n")
        fout.write("<th width='10'> </th>\n")
        fout.write("<th>播放量</th>\n")
        fout.write("<th>创建人</th>\n")
        fout.write("<th>创建人ID</th>\n")
        fout.write("<th width='10'> </th>\n")
        fout.write("<th>歌单封面</th>\n")
        fout.write("<th>歌单位置</th>\n")
        i = 0
        for data in self.datas:
            i = i+1
            fout.write("<tr>\n")
            #排名
            fout.write("<td align='center'>\n%d</td>" %i)
            #歌单名
            fout.write("<td align='left'>\n<a href=%s>%s</a>\n</td>\n"%("http://music.163.com"+data[1], data[0]))
            #歌单ID
            fout.write("<td align='center'>%s</td>\n"%data[1].replace("/playlist?id=",""))
            #空列
            fout.write("<td width='10'></td>")
            #播放量
            fout.write("<td align='center'>%s</td>\n"%data[2])
            #创建人
            fout.write("<td align='center'>\n<a href=%s>%s</a>\n</td>\n"%("http://music.163.com"+data[4], data[3]))
            #创建人ID
            fout.write("<td align='center'>%s</td>\n"%data[4].replace("/playlist?id=","").replace("/user/home?id=",""))
            #空列
            fout.write("<td width='10'></td>")
            #歌单封面
            fout.write("<td align='center'>\n<a href=%s><img src=%s width='60' hight='60'></a>\n</td>\n" %("http://music.163.com"+data[1], data[5]))
            #歌单位置
            fout.write("<td align='center'>\nPage:%d No:%d</td>" %(data[6], data[7]))
            fout.write("</tr>\n")
        
        fout.write("</table>\n")
        fout.write("</body>\n")
        fout.write("</html>\n")
        
        fout.close()

    
    def output_excel(self):

        with codecs.open("test1.csv", "w+", "utf_8_sig") as csvfile:
            cfile = csv.writer(csvfile, dialect="excel")
            cfile.writerow(['歌单名','歌单ID','播放量','创建人','创建人ID','歌单封面'])
            for data in self.datas:
                cfile.writerow([data[0], data[1].replace("/playlist?id=",""), data[2], data[3], 
                                data[4].replace("/playlist?id=","").replace("/user/home?id=",""), 
                                data[5], data[6], data[7]])
            
    
    
    
    
    



