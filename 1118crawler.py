import requests
from bs4 import BeautifulSoup

# re = requests.get('https://www.ccclub.io/course/2020Fall')
# print(re.status_code)
# # print(re.text)
# soup = BeautifulSoup(re.text, 'html.parser')
# body = soup.tbody
# # print(soup.tr)
# # print(body)
# # print(body.find_all('tr')[1])
# # print(type(body.find_all('tr')))
# for tr in body.find_all('tr'):
#     # print(tr.find_all('td')[2])
#     if 'announce' in tr.find_all('td')[2].text:
#         print(tr.find_all('td')[1].text)
#     # print(tr.find_all('td')[2].string)

# re = requests.get('https://ifoodie.tw/explore/list/%E9%A4%90%E9%85%92%E9%A4%A8%2F%E9%85%92%E5%90%A7')
# print(re.status_code)
# soup = BeautifulSoup(re.text, 'html.parser')
# soup.find('div', {'class': 'b-ent'})
# for row in soup.find_all('div', {'class': 'restaurant-info'}):
#     avg_price = row.find('div', {'class': 'avg-price'}).text
#     # num = row.find('div', {'class': 'board-nuser'}).text
#     print(avg_price.split(' '))


url = 'https://ifoodie.tw/explore/list/餐酒館%2F酒吧'
resp = requests.get(url)
# print(re.status_code)
# 餐廳名 title-text
# 評價星等 rating-star level-5 responsive
# 均消 avg-price
# 營業時間：需要點進餐廳頁面
# openingHourList 下面：
# 當天 weekday-hours today, 其他天 weekday-hours
soup = BeautifulSoup(resp.text, 'html.parser')
for row in soup.find_all('div', {'class': 'title-row'}):
    restaurant_title = row.find('div', {'class':'title'}).text
    print(restaurant_title)
for row in soup.find_all('div', {'class': 'jsx-2133253768'}):
    rating_star = row.find('div', {'class':'jsx-1207467136 text'})
    if rating_star == None:
        pass
    else:
        print(rating_star.text)
