from selenium import webdriver
import chromedriver_autoinstaller
import time
import datetime

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('ignore-certificate-errors')
try:
    driver = webdriver.Chrome("/Users/jeongwle/Downloads/chromedriver", options=options)
    # driver = webdriver.Chrome("/Users/jeongwle/Downloads/chromedriver")
except:
    path = chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(path, options=options)

driver.implicitly_wait(10)
driver.get(url='http://prod.danawa.com/list/?cate=11338057')
total = int(driver.find_element_by_css_selector(
    '#danawa_content > div.product_list_wrap > div > div.prod_list_tab > ul > li.tab_item.selected > a > strong.list_num').text.strip('()'))
idx = 0
name = list(range(0, total))
price = list(range(0, total))
date = list(range(0, total))
review = list(range(0, total))
link = list(range(0, total))
pcode = list(range(0, total))
li_list = driver.find_elements_by_css_selector(
    '#productListArea > div.main_prodlist.main_prodlist_list > ul > li.prod_item.prod_layer[id]') #[id]는 li.prod_item.prod_layer중 id를 가진애들만 한다는 뜻
for product in li_list:
    name[idx] = product.find_element_by_css_selector('div > div.prod_info > p > a').text
    price[idx] = product.find_element_by_css_selector('div > div.prod_pricelist > ul > li > p.price_sect > a > strong').text
    date[idx] = product.find_element_by_css_selector('div > div.prod_sub_info > div > dl.meta_item.mt_date > dd').text
    try :
        review[idx] = product.find_element_by_css_selector('div > div.prod_sub_info > div > dl.meta_item.mt_comment > dd > a > strong').text
    except :
        review[idx] = str(0)
    # review[idx] = str(0)
    link[idx] = str(product.find_element_by_css_selector('div > div.prod_info > p > a').get_attribute('href'))
    pcode[idx] = str(product.get_attribute('id')).lstrip('productItem')
    idx += 1
    # print ('='*50)
    # print('제품명 : {}'.format(name))
    # if price[idx] == '일시품절' or price[idx] == '출시예정':
        # print(price[idx] + '-')
    # else:
    #     print('가격 : {}원'.format(price))
    # print('등록월 : {}'.format(date))
    # print('상품의견 : {}건'.format(review))
try:
    next_page = driver.find_element_by_css_selector('#productListArea > div.prod_num_nav > div > div > a:nth-child(2)')
except:
    driver.quit()
is_next = next_page.is_enabled()
# next_page.click()
# time.sleep(1)
# page = driver.find_element_by_css_selector('#productListArea > div.prod_num_nav > div > a').text
# print(page)
while (is_next == True):
    print('='*40, '다음페이지', '='*40)
    next_page.click()
    time.sleep(2)
    li_list = driver.find_elements_by_css_selector(
    '#productListArea > div.main_prodlist.main_prodlist_list > ul > li.prod_item.prod_layer[id]') #[id]는 li.prod_item.prod_layer중 id를 가진애들만 한다는 뜻
    time.sleep(1)
    for product in li_list:
        name[idx] = product.find_element_by_css_selector('div > div.prod_info > p > a').text
        price[idx] = product.find_element_by_css_selector('div > div.prod_pricelist > ul > li > p.price_sect > a > strong').text
        date[idx] = product.find_element_by_css_selector('div > div.prod_sub_info > div > dl.meta_item.mt_date > dd').text
        try :
            review[idx] = product.find_element_by_css_selector('div > div.prod_sub_info > div > dl.meta_item.mt_comment > dd > a > strong').text
        except :
            review[idx] = str(0)
        # review[idx] = str(0)
        link[idx] = str(product.find_element_by_css_selector('div > div.prod_info > p > a').get_attribute('href'))
        pcode[idx] = str(product.get_attribute('id')).lstrip('productItem')
        idx += 1
        # print ('='*50)
        # print('제품명 : {}'.format(name))
        # if price[idx] == '일시품절' or price[idx] == '출시예정':
        #     print(price[idx] + '-')
        # else:
        #     print('가격 : {}원'.format(price))
        # print('등록월 : {}'.format(date))
        # print('상품의견 : {}건'.format(review))
    page = driver.find_element_by_css_selector('#productListArea > div.prod_num_nav > div > div > a.num.now_on').text
    if int(page) % 10 == 0:
        try:
            next_page = driver.find_element_by_css_selector('#productListArea > div.prod_num_nav > div > a')
        except:
            break
    else:
        try:
            next_page = driver.find_element_by_css_selector('#productListArea > div.prod_num_nav > div > div > a:nth-child(%s)'%(int(page)%10 + 1)) 
            # int(page)를 10의 나머지로 하는 이유는 다나와가 11페이지도 1페이지로 인식해서
        except:
            break
    is_next = next_page.is_enabled()
driver.quit()

results = [[0 for j in range(7)]for i in range(total)]
idx = 0
for i in range(total):
    results[idx][0] = name[idx]
    if price[idx] == '일시품절' or price[idx] == '출시예정':
        results[idx][1] = 0
        results[idx][2] = price[idx]
    else:
        results[idx][1] = int(price[idx].replace(",", ""))
        results[idx][2] = '판매중'
    results[idx][3] = date[idx]
    results[idx][4] = int(review[idx].replace(",", ""))
    results[idx][5] = link[idx]
    results[idx][6] = pcode[idx]
    idx += 1
today = datetime.datetime.now().strftime('%Y.%m.%d')

import pymysql

conn = pymysql.connect(
    user = "jeongwle",
    password = "1q2w3E4R!",
    host = "localhost",
    db = "NINTENDO"
)
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS switchtitle (number int auto_increment, title varchar(100), status varchar(20), release_date varchar(20), link varchar(100), pcode varchar(20), PRIMARY KEY (number), UNIQUE KEY (pcode))")
cursor.execute("CREATE TABLE IF NOT EXISTS price (number int auto_increment, product_id int, price int, modified_date varchar(20), PRIMARY KEY (number), FOREIGN KEY (product_id) REFERENCES switchtitle (number))")
cursor.execute("CREATE TABLE IF NOT EXISTS review (number int auto_increment, product_id int, review int, modified_date varchar(20), PRIMARY KEY (number), FOREIGN KEY (product_id) REFERENCES switchtitle (number))")
idx = 0
for i in range(total):
    return_value = cursor.execute("SELECT * FROM switchtitle WHERE pcode = '%s'" %results[idx][6])
    if (return_value == 1):
    # try :
        cursor.execute("UPDATE switchtitle SET status = '%s' WHERE pcode = '%s'" %(results[idx][2], results[idx][6]))
    # except :
    else :
        cursor.execute(
            f'INSERT INTO switchtitle(title, status, release_date, link, pcode) VALUES(\"{results[idx][0]}\", \"{results[idx][2]}\", \"{results[idx][3]}\", \"{results[idx][5]}\", \"{results[idx][6]}\")'
            )
    cursor.execute(f"INSERT INTO price(product_id, price, modified_date) VALUES((SELECT number from switchtitle where pcode = \"{results[idx][6]}\"), \"{results[idx][1]}\", \"{today}\")")
    cursor.execute(f"INSERT INTO review(product_id, review, modified_date) VALUES((SELECT number from switchtitle where pcode = \"{results[idx][6]}\"), \"{results[idx][4]}\", \"{today}\")")
    idx += 1
conn.commit()
conn.close()
# # # import pandas as pd

# # # data = pd.DataFrame(results)
# # # data.columns = ['title', 'price', 'date', 'review']
# # # data.to_csv('스위치타이틀_cp949.csv', encoding='cp949') 