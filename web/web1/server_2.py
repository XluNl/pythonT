
#http://www.cnblogs.com/yuanchenqi/articles/6083427.html

from wsgiref.simple_server import make_server
#import  wsgiref.simple_server
def f1(environ):
    return [b'<h1>Hello,book</h1>',b'<h1>Hello,book</h1>']
def f2(environ):
    return [b'<h1>Hello,web!</h1>']

def application(environ, start_response):
    #print(environ)
    path_info = environ['PATH_INFO']
    #start_response 设置heard头信息
    start_response('200 OK', [('Content-Type', 'text/html')])
    if path_info =='/book':
        return f1(environ)
    elif path_info=='/web':
        return f2(environ)
    else:
        return [b'<h1>404</h1>']

httpd = make_server('localhost', 8089, application)

print('Serving HTTP on port 8088...')
# 开始监听HTTP请求:
httpd.serve_forever()