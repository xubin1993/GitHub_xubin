#coding=utf-8
import re
import urllib2
import provincial_city
import urllib
import time
from OpenPage import OpenPage
from lxml import etree
import json
import chardet
import codecs
laji=['fangchan','soufang','xinlangleju','anjuke','dianping','dingcanmishu','tongcheng','xiecheng','baidulvyou']
class BAIDUMAP_ADDRESS():
    def __init__(self):
        self.city_list=[]
        self.open_page=OpenPage()
        self.bibi=[]
        self.qu_list={
    "佛山市":["高明市"]# 此处可以放市区，字典格式
    }
    def panduan(self,a,f):
        if a:
            if a[0]!='':
                print a[0]
                f.write(a[0])
                f.write('BBD')
            else:
                print '无'
                f.write('无')
                f.write('BBD')
        else:
            print '无'
            f.write('无')
            f.write('BBD')

    def get_xy(self,url):#根据地址获取经纬度
        print url
        count=10
        while (True):
            try:
                myPage=self.open_page.Openpage(url)
                break
            except Exception as e3:
                print e3
                if count<=0:
                    raise  Exception(u"连续10次失败,放弃")
                count-=1
                time.sleep(1)
        x_y=re.findall('{"lng":(.*?),"lat":(.*?)}',myPage)
        print x_y
        return x_y
    def get_message(self,i,url,f,city_list):#获取写字楼名称，地址，标签，价格，容积率，开发商，电话等
        count=10
        while (True):
            try:
                myPage=self.open_page.Openpage(url)
                break
            except Exception as e3:
                print e3
                if count<=0:
                    raise  Exception(u"连续10次失败,放弃")
                count-=1
                time.sleep(1)
        try:
            myPage=unicode(myPage,'unicode-escape')#asc 转unicode
            myPage=myPage.encode('utf-8')
            #myPage=myPage.decode('utf-8')
            message_list=myPage.split('"acc_flag":0')



            for m in range(1,len(message_list)):
                add=''
                address=re.findall('"addr":"(.*?)"',message_list[m],re.S)

                name=re.findall('"name":"(.*?)"',message_list[m],re.S)
                tel=re.findall('"tel":"(.*?)"',message_list[m])
                tag=re.findall('"tag":"(.*?)"',message_list[m])
                aoi=re.findall('"aoi":"(.*?)"',message_list[m])
                building_time=re.findall('"building_time":"(.*?)"',message_list[m])
                # #"price":"10475.0","price_change_rate":"-0.0648","property_company":"","property_management_fee":"3.5","property_right":"","rent_price":"42"
                #"volume_rate":"2.60"
                volume_rate=re.findall('"volume_rate":"(.*?)"',message_list[m])
                developers=re.findall('"developers":"(.*?)"',message_list[m])
                # "developers":"\u4e1c\u839e\u8de8\u65e5\u6295\u8d44\u6709\u9650\u516c\u53f8"
                house_type=re.findall('"house_type":"(.*?)"',message_list[m])
                #"house_type"
                B=[]
                f.write(i)
                f.write('BBD')
                for p in name:
                    if p not in laji and p not in B and p not in city_list:
                        print p
                        names=p
                        f.write(p)
                        B.append(p)
                f.write('BBD')
                for p in address:
                    if p not in city_list:
                        add=add+p
                        f.write(p)
                        print p
                f.write('BBD')
                data2={'address':add}
                #print data2
                data2=urllib.urlencode(data2)
                xy_url='http://api.map.baidu.com/geocoder/v2/?%s&output=json&ak=（此处为百度地图API开发者密钥，详情参照百度地图API）'%data2
                xy=self.get_xy(xy_url)
                if xy:
                    for h in xy:
                        f.write(h[0])
                        f.write('BBD')
                        f.write(h[1])
                        f.write('BBD')
                else:
                    data2={'address':names}
                    #print data2
                    data2=urllib.urlencode(data2)
                    xy_url='http://api.map.baidu.com/geocoder/v2/?%s&output=json&ak=（此处为百度地图API开发者密钥，详情参照百度地图API）'%data2
                    xy=self.get_xy(xy_url)
                    if xy:
                        for h in xy:
                            f.write(h[0])
                            f.write('BBD')
                            f.write(h[1])
                            f.write('BBD')
                    else:
                        f.write('无')
                        f.write('BBD')
                        f.write("无")
                        f.write('BBD')



                self.panduan(aoi, f)
                self.panduan(tel, f)
                self.panduan(building_time,f)
                self.panduan(developers,f)
                self.panduan(house_type,f)
                self.panduan(volume_rate,f)
                f.write('\r\n')
        except Exception as e2:
            print e2


    def get_Company_name(self,key):#
        city_list=[]
        self.city_list=self.qu_list.keys()
        for i in self.city_list:
            r=self.qu_list.get(i)
            for m in r:
                city=i+' '+m+' 写字楼'
                city_list.append(city)


        f=codecs.open('data2.txt','a+')
        for i in city_list:
            j=0
            key=1
            if i not in self.bibi:
                self.bibi.append(i)

                while (j<30):
                    print i
                    try:
                        #url='http://api.map.baidu.com/?qt=s&c=131&wd=%E4%B8%9C%E8%8E%9E%E5%B8%82%20%E5%86%99%E5%AD%97%E6%A5%BC&rn=10&ie=utf-8&oue=1&res=api&callback=BMap._rd._cbk10734'
                        data={"qt":'s','c':131,'wd':i,'rn':10,'pn':j,'ie':'utf-8','oue':'1','res':'api','callback':'BMap._rd._cbk98503'}
                        data=urllib.urlencode(data)
                        url='http://api.map.baidu.com/?'+data
                        print url
                        self.get_message(i, url,f,city_list)
                        j=j+1
                    except Exception as e2:
                        print e2
                        self.get_message(i, url,f,city_list)
        f.close()

if __name__=="__main__":
    ss=BAIDUMAP_ADDRESS()
    ss.get_Company_name(1)
    
