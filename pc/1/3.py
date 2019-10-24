#__author: xlu.com
#date : 2018/8/1

from urllib import request,parse
from http.cookiejar import CookieJar

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Referer"   :"http://www.renren.com/SysHome.do",
    'Cookie': 'anonymid=jkahptzv-4cez42; depovince=BJ; _r01_=1; JSESSIONID=abcOeLvTQNXfLeeUhpZtw; ick_login=2eac8240-2570-44cf-be72-aeea9b93970c; wp=0; vip=1; ick=969f2b63-77db-436b-b38c-361026821ccf; XNESSESSIONID=cf5f61fb6e52; jebe_key=ad3a36ae-0210-4736-b424-8ff3f2093a59%7C1a11203847f6ae0e05e3590c05179f6c%7C1533089651681%7C1%7C1533089519224; first_login_flag=1; ln_uact=18810564556; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; loginfrom=syshome; wp_fold=0; jebecookies=f26bb4ce-17f7-4eb8-9c95-581f5cbf7731|||||'
}
#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
def get_opener():
    cookiejar = CookieJar(filename)
    # 使用cookie创建一个http对象
    handler = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(handler)
    return opener

#1先登录
def rr_login(opener):
    data = {
        'email': '18810564556',
        'icode':'',
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': '1',
        'captcha_type': 'web_login',
        'password': '4ced13c48cc7c91a9d0ddbcfb069d0d98ce70897925ad46d95e2fbdbd7b8a17c',
        'rkey': 'd5ff51375d8eb17a011cad5622d835fd',
        'f': 'http%3A%2F%2Fzhibo.renren.com%2Ftop'
    }
    login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018731131144'
    # login_url = 'http://www.renren.com/ajaxLogin/login'
    data = parse.urlencode(data).encode("utf-8")
    req = request.Request(login_url,headers=headers,data=data,method='POST')
    resp =opener.open(req)
    # resp = request.urlopen(req)
    # print(resp)
    # exit()

#2访问主页
def rr_index(opener):
    index_url = "http://zhibo.renren.com/top"
    # 获取个人主页的的时候 使用之前的那个opener，因为已经包含了需要的cookie信息
    req = request.Request(index_url,headers=headers)
    resp = opener.open(req)
    with open('renren.html','w',encoding='utf-8',) as fp:
        fp.write(resp.read().decode('utf-8'))

if __name__ == '__main__':
    opener = get_opener()
    rr_login(opener)
    # rr_index(opener)