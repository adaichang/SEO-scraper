from array import *
import requests
import csv
import urllib2
from lxml import etree


class csvImport:
    def __init__(self,filename):
        self.filename = filename

    def retrieveDataFromCSV (self):
            my_content=[]
            if not my_content:
                with open(self.filename,'rb') as ifile:
                    reader=csv.reader(ifile)
                    next(reader)
                    included_cols=[0, 1, 2, 3]
                    fields = ['page_url','title','meta_description','content']
                    xpath = [{field: row[i] for field, i in zip(fields, included_cols)} for row in reader]
                    return xpath

    def enterCSVFile(self):
        url_list = []
        if not url_list:
            myCSVContent = retrieveDataFromCSV ('test_store_file.csv')
            for y in myCSVContent:
              url_lists = y[0]


# (k, v), = url_listing[0].items()
#    print k
# url_listing = csvImport('test_xpath.csv').retrieveDataFromCSV()



class XpathParser:
    def __init__(self):
        pass

    def sendRequest(self,link):
        print('sending request to '+ link)
        html = requests.get(link,timeout=5).text.encode(encoding='UTF-8',errors='strict')
        print('request completed')
        html = "".join(html.split("\n"))
        html = "".join(html.split("\t"))
        html = " ".join(html.split("  "))
        html = " ".join(html.split("  "))
        return html

    def load(self,links,xpath):
        url=links.split("\r\n")
        data = {}
        data['scrapResult'] = []
        for link in url:
            tree = etree.HTML(self.sendRequest(link))
            result = {}
            result["link"] = link
            result["result"] = self.start(tree,xpath)
            data['scrapResult'].append(result)
        return data

    def start(self,tree,xpath):
        result = []
        for data in xpath['scrap']:
            if data['name'] and data['value']:
                dect = {}
                value,name = "",""
                name = data['name']
                element = tree.xpath(data['value'])
                if len(element):
                    print(element)
                    value = element[0].text
                    if not value:
                        value = etree.tostring(element[0])
                dect['name'] = name
                dect['value'] = value
                result.append(dect)
        return result


url_listing = csvImport('test_config.csv').retrieveDataFromCSV()
url = []
title_xpath = []
description_xpath = []
caption_xpath = []

for url_listing_lists in url_listing:
    page_url_topic, page_url = url_listing_lists.items()[3]          #[3] page url , [2] title , [1] caption  [0] metadescription
    url.append(page_url)

for title_listing_lists in url_listing:
    title, title_xpath_data = title_listing_lists.items()[2]          #[3] page url ; [2] title ; [1] caption ; [0] metadescription
    title_xpath.append(title_xpath_data)

for meta_description_listing_lists in url_listing:
    meta_descriptioin_topic, description_xpath_data = meta_description_listing_lists.items()[0]          #[3] page url ; [2] title ; [1] caption ;  [0] metadescription
    description_xpath.append(description_xpath_data)

for caption_listing_lists in url_listing:
    caption_topic, caption_xpath_data = caption_listing_lists.items()[1]          #[3] page url ; [2] title ; [1] caption ; [0] metadescription
    caption_xpath.append(caption_xpath_data)

print title_xpath
print description_xpath
print caption_xpath
print url

import sys
filename = 'dynamic_url.csv'
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
           	r1 =str(row)[1:-1]
		print r1
		slashparts = r1.split('/')
		basename = '/'.join(slashparts[:3]) + '/'
# All except the last one
		dirname = '/'.join(slashparts[:-1]) + '/'
		print 'slashparts = %s' % slashparts
		print 'basename = %s' % basename
		print 'dirname = %s' % dirname
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
print row
import os
import errno

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST or not os.path.isdir(path):
            raise
# url=["http://www.w3schools.com/","http://www.w3schools.com/html/default.asp"]
# url="http://www.w3schools.com/"
# url="http://www.w3schools.com/html/default.asp"
# xpath = {'scrap':[{'name':'title','value':'/html/head/title'},                        #main portion
#                {'name':'meta_description','value':'/html/head/meta[2]'},
#                {'name':'caption_field','value':'//*[@id="c4tab1"]'}]}
# xpath = {'scrap':[{'name':'header_text','value':'/html/body/div[1]/div'},
#                 {'name':'title','value':'/html/head/title'}]}

# for urls in url:
    # xpath = {'scrap':[{'name':'title','value':'/html/head/title'},
    #                {'name':'meta_description','value':'/html/head/meta[2]'},
    #                {'name':'caption_field','value':'//*[@id="c4tab1"]'}]}
    # print(XpathParser().load(urls,xpath))
    # print(XpathParser().load(url_seperator[1],xpath))
    # print (XpathParser().load(urls,xpath))