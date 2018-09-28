import os
import sys
import time
import random
import pprint

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from MagicGoogle import MagicGoogle
from pyquery import PyQuery as pq

################################################
# """
# cd MagicGoogle
# python Examples/search_result.py
# """
#################################################


#将读取的网页以网页的形式存储到本地文件
def storageToLocalFiles(storagePath, data):
    fhandle = open(storagePath,"wb")
    fhandle.write(data)
    fhandle.close()

storagePath = "./"


#export http_proxy=http://127.0.0.1:1087;
#export https_proxy=http://127.0.0.1:1087;

PROXIES = [{
    'http': 'http://127.0.0.1:1087',
    'https': 'http://127.0.0.1:1087'
}]

#keyword_list = ['big data','liuqiangdong','jingdong']
keyword_list = ['wangqishan','Donald Trump','刘强东性侵','jinzhengen','iran','russia israel']
#mg = MagicGoogle()
mg = MagicGoogle(PROXIES)

# The first page of results
# result = mg.search_page(query='python')
# print(result)
#
# time.sleep(random.randint(1, 5))

# Get {'title','url','text'}


from urllib import request
    

def read_pageHtml(url):
    file = request.urlopen(url)
    data = file.read()
    return data

for keywords in keyword_list:
    print(' --- --- --- >' + keywords)
#    os.mkdir(keywords) 创建关键字目录
    ndir = os.mkdir(storagePath + keywords)
    os.chdir(storagePath + keywords)
    for content in mg.search(query=keywords, language='en'):
        pprint.pprint(content)
        if(content['title'] == '' or content['text'] == '' or content['url'] == None or content['url'] == ''):
            continue
        doc = mg.get_page_file(content['url'])
        storageToLocalFiles(storagePath + content['title'] +'.html', doc)
        
        time.sleep(random.randint(1, 5))
    os.chdir("..") #换路径




#for keywords in keyword_list:
#    print(keywords)
##    for i in mg.search(query=keywords, num=1, language='en'):
##        pprint.pprint(i)
#    for url in mg.search_url(query=keywords):
#        pprint.pprint(url)
#        time.sleep(random.randint(1, 5))
        
        
# Output
# {'text': 'The official home of the Python Programming Language.',
# 'title': 'Welcome to Python .org',
# 'url': 'https://www.python.org/'}

# Get first page
#for url in mg.search_url(query='python'):
#    pprint.pprint(url)
#
#time.sleep(random.randint(1, 5))

# Output
# 'https://www.python.org/'
# 'https://www.python.org/downloads/'
# 'https://www.python.org/about/gettingstarted/'
# 'https://docs.python.org/2/tutorial/'
# 'https://docs.python.org/'
# 'https://en.wikipedia.org/wiki/Python_(programming_language)'
# 'https://www.codecademy.com/courses/introduction-to-python-6WeG3/0?curriculum_id=4f89dab3d788890003000096'
# 'https://www.codecademy.com/learn/python'
# 'https://developers.google.com/edu/python/'
# 'https://learnpythonthehardway.org/book/'
# 'https://www.continuum.io/downloads'

# Get second page
#for url in mg.search_url(query='python', start=10):
#    pprint.pprint(url)

# Output
# 'https://github.com/python'
# 'https://github.com/python/cpython'
# 'https://www.learnpython.org/'
# 'https://www.raspberrypi.org/documentation/usage/python/'
# 'https://www.reddit.com/r/Python/'
# 'https://www.datacamp.com/courses/intro-to-python-for-data-science'
# 'https://www.coursera.org/learn/python'
# 'https://www.coursera.org/learn/interactive-python-1'
# 'http://abcnews.go.com/US/record-breaking-17-foot-python-captured-south-florida/story?id=51616851'
# 'https://hub.docker.com/_/python/'
