#coding=utf-8
import urllib2
import urllib
import re
import sys
import random
#from OpenPage1 import Openpage
class OpenPage():
    def Openpage(self,url):
        #data = urllib.urlencode(data)
        #print data
        try:
            user_agents = [
                'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
                'Opera/9.25 (Windows NT 5.1; U; en)',
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
                'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
                "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
                "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/36.0 ",
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100103 Firefox/37.0',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
                'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.7',
                'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.6',
                'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.1',
                'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.2',
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100103 Firefox/35.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/36.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/37.0',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/38.0', 

            ]
            opener = urllib2.build_opener(urllib2.HTTPHandler)
            agent = random.choice(user_agents)
            opener.addheaders = [("User-agent",agent),('Host','http://www.google.cn'),("Accept","*/*")]

            req = urllib2.Request(url)
            response =opener.open(req)
            the_page = response.read()
            print the_page
            f=open('2.txt','w+')
            f.write(the_page)
            f.close()
        except Exception as e2:
            print e2
            self.Openpage(url)
#url='http://www.google.cn/maps/search/%E5%B9%BF%E5%B7%9E%E5%86%99%E5%AD%97%E6%A5%BC'
#data={'address':'天河区天河路490号，与天河东路交界处东南侧 '}
#data=urllib.urlencode(data)
#url='http://api.map.baidu.com/geocoder/v2/?%s&output=json&ak=1841497dd6f3b767a7324b6d95f6077b'%data
#print url
#ss=OpenPage()
#ss.Openpage(url)
