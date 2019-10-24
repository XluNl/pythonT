#__author: xlu.com
#date : 2018/10/26
import re
import requests
if __name__ == '__main__':
    str = '1234534321'
    res = re.search(r'3',str)
    print(res.group())

    res = re.findall('3',str)
    print(res)

    str = """<div class="allBoxes">
                <div class="allmoreunder">
                        <img src="/static/images/index/Mask2.png" alt="" class="allBoxesImg"/>
                        <a href="{:url('index/catering/index')}">
                            werwe<p class="moreunder">了解更多</p>
                        </a>
                </div>
                <div class="allp">
                    <p class="allBoxesP1 overflow">餐饮行业</p>
                    <p class="allBoxesP2 overflowTwo">线上线下互通，业绩翻倍增长</p>
                </div>
                <p class="allBoxesP2 overflowTwo">查我啊</p>
                <img src="" alt="二维码" class="caseWimBoxBotImg"/>
                <div class="caseWimBoxBotBj"></div>
            </div>"""
    res = re.search(r'<p .*?>(?P<id>.*?)</p>',str,re.DOTALL)
    print(res.group('id'))
    # res = re.findall(r'<div .*?<p.*?>(.*?)</p>.*?</div>',str,re.DOTALL)
    res = re.findall(r'<div class="allp">(.*?)</div>',str,re.DOTALL)
    # res = re.findall(r'<p.*?>(.*?)</p>',str,re.DOTALL)
    print(res[0])
    res = re.findall(r'\n.*?<p.*?>(.*?)</p>.*?',res[0],re.DOTALL)
    print(res[0])

    resp = requests.get('https://www.baidu.com')
    html = resp.content.decode('utf-8')
    print(html)