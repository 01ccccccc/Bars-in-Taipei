import requests
from urllib.parse import urlencode, urljoin
from bs4 import BeautifulSoup
import pandas as pd
import time
# from selenium import webdriver

# driver = webdriver.Chrome('/Users/hazel_lin/Documents/GitHub/Bars-in-Taipei/chromedriver')
# from selenium.webdriver.chrome.options import Options

# my_options = Options()
# my_options.add_argument("--incognito")

# driver = webdriver.Chrome(options = my_options)

def ifood_url(location, kind, page):
    paras_loc = {'location': location}
    paras_kind = {'kind': kind}
    paras_page = {'page': page}

    loc = urlencode(paras_loc).split('=')[-1]
    kind = urlencode(paras_kind).split('=')[-1]
    
    url = f'https://ifoodie.tw/explore/{loc}/list/{kind}?{urlencode(paras_page)}'
    return url

r = requests.get(ifood_url('台北市','餐酒館/酒吧', '1'))
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify)
# 營業時間、平均消費額

# link = soup.find('a',{'class':'jsx-2133253768 title-text'})
# a_tags = soup.find_all('a',{'class':'jsx-2133253768 title-text'})
# for tag in a_tags:
#     print(tag.get('href'))
# print(link)
page = 1
dct = {'name':[], 'address':[], 'avg_price':[], 'link':[]} # 店名、地址相同屬性可merge # 均價部分把「均價」文字去掉只留下價格 #營業時間需點進link，先存link進字典

while page < 30:
    r = requests.get(ifood_url('台北市','餐酒館/酒吧', page))
    soup = BeautifulSoup(r.text, 'html.parser')

    for name, address, avg_price, link in zip(soup.find_all('a', {'class':'jsx-2133253768 title-text'}), 
                                              soup.find_all('div', {'class':'jsx-2133253768 address-row'}), 
                                              soup.find_all('div', {'class':'jsx-2133253768 avg-price'}), 
                                              soup.find_all('a', {'class':'jsx-2133253768 title-text'})):
        price_lst = avg_price.get_text().split()

        dct['name'].append(name.text)
        dct['address'].append(address.text)
        dct['avg_price'].append(price_lst[-1])
        dct['link'].append(f'https://ifoodie.tw{link.get("href")}')
    page += 1

    time.sleep(2)
    # r1 = driver.get(f'https://ifoodie.tw{link.get("href")}')
    # time.sleep(5)
    # info = driver.find_element_by_class_name('jss76')
    # info.click()
    # print(info)
    # soup1 = BeautifulSoup(r1.page_source, 'html.parser')
    
    # for business_hour in soup1.find_all('div',{'class':'jss182 weekday-hours'}):
    #     dct['business_hour'].append(business_hour.text)
    # driver.close()

# print(dct)
df = pd.DataFrame(dct)

print(df)