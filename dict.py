#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import re
import sys

def downloadfromyoudao(url,patterns):
    response = urllib2.urlopen(url)
    responseHtml = response.read()

    #responseHtml = responseHtml.decode("gbk").encode("utf-8")

    pattern = re.compile(patterns,re.S)
    item_list = pattern.findall(responseHtml)

    for item in item_list:
        if "</li>" in item:
            item = item.replace("<li>","").replace("</li>","").replace(' ','').replace('\n','')
            print item
            break
        else:
            print 'not find the word'
            break
    print "=========================================="

def downloadfromiciba(url,patterns):
    response = urllib2.urlopen(url)
    responseHtml = response.read()

    #responseHtml = responseHtml.decode("gbk").encode("utf-8")

    pattern = re.compile(patterns,re.S)
    item_list = pattern.findall(responseHtml)

    for item in item_list:
        if "</li>" in item:
            item = item.replace('<li class="clearfix">',"").replace('</li>','').replace('<span class="prop">','').replace('<span>','').replace('</span>','').replace('<p>','').replace('</p>','').replace(' ','').replace('\n','')
            print item
            break
        else:
            print 'not find the word'
            break
    print "=========================================="

def main(hello):
    print 'iciba: ' + hello
    downloadfromiciba("http://www.iciba.com/" + hello,'<ul class="base-list switch_part" class="">(.*?)</ul>')
    print 'youdao: ' + hello
    downloadfromyoudao("http://dict.youdao.com/w/eng/" + hello,'<ul>(.*?)</ul>')

if __name__ == '__main__':
    len = len(sys.argv)
    if len>1:
        for i in range(1,len):
            main(sys.argv[i])
    else:
        hello = raw_input('input a word: ')
        main(hello.strip())
