#__author: xlu.com
#date : 2019/10/16

from gevent import monkey; monkey.patch_all()
import gevent
from  urllib.request import urlopen
import time
from gevent import monkey

#重点(最大程度 切换)
# monkey.patch_all()

def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

if __name__ == "__main__":
    start = time.time()

    urls = ['https://www.python.org/','https://www.yahoo.com/','https://github.com/']
    for url in urls:
        f(url)

    # gevent.joinall([
    #         gevent.spawn(f, 'https://www.python.org/'),
    #         gevent.spawn(f, 'https://www.yahoo.com/'),
    #         gevent.spawn(f, 'https://github.com/'),
    # ])
    print(time.time()-start)