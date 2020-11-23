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

re = requests.get('https://ifoodie.tw/explore/list/%E9%A4%90%E9%85%92%E9%A4%A8%2F%E9%85%92%E5%90%A7')
print(re.status_code)
soup = BeautifulSoup(re.text, 'html.parser')
soup.find('div', {'class': 'b-ent'})
for row in soup.find_all('div', {'class': 'restaurant-info'}):
    avg_price = row.find('div', {'class': 'avg-price'}).text
    # num = row.find('div', {'class': 'board-nuser'}).text
    print(avg_price.split(' '))