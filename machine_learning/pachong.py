import requests
from bs4 import BeautifulSoup
# requests返回网页内容
res = requests.get(r'https://xm.esf.fang.com/house-a0352/')
#res.text

# BeautifulSoup解析网页
soup = BeautifulSoup(res.text,'html.parser') # 使用 HTML.parser 解析器