from selenium import webdriver
import chromedriver_autoinstaller
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
try:
    driver = webdriver.Chrome("/Users/jeongwle/Downloads/chromedriver", options=options)   
    # driver = webdriver.Chrome("/Users/jeongwle/Downloads/chromedriver")
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome("/Users/jeongwle/Downloads/chromedriver", options=options)

driver.implicitly_wait(3)
driver.get(url='http://prod.danawa.com/list/?cate=11338057')
li_list = driver.find_elements_by_css_selector(
    '#productListArea > div.main_prodlist.main_prodlist_list > ul > li.prod_item.prod_layer[id]') #[id]는 li.prod_item.prod_layer중 id를 가진애들만 한다는 뜻
for product in li_list:
    name = product.find_element_by_css_selector('div > div.prod_info > p > a').text
    price = product.find_element_by_css_selector('div > div.prod_pricelist > ul > li > p.price_sect > a > strong').text
    date = product.find_element_by_css_selector('div > div.prod_sub_info > div > dl.meta_item.mt_date > dd').text
    try :
        review = product.find_element_by_css_selector('div > div.prod_sub_info > div > dl.meta_item.mt_comment > dd > a > strong').text
    except :
        review = str(0)
    print ('='*50)
    print('제품명 : {}'.format(name))
    if price == '일시품절' or price == '출시예정':
        print(price)
    else:
        print('가격 : {}원'.format(price))
    print('등록월 : {}'.format(date))
    print('상품의견 : {}건'.format(review))
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
        name = product.find_element_by_css_selector('div > div.prod_info > p > a').text
        price = product.find_element_by_css_selector('div > div.prod_pricelist > ul > li > p.price_sect > a > strong').text
        date = product.find_element_by_css_selector('div > div.prod_sub_info > div > dl.meta_item.mt_date > dd').text
        try :
            review = product.find_element_by_css_selector('div > div.prod_sub_info > div > dl.meta_item.mt_comment > dd > a > strong').text
        except :
            review = str(0)
        print ('='*50)
        print('제품명 : {}'.format(name))
        if price == '일시품절' or price == '출시예정':
            print(price)
        else:
            print('가격 : {}원'.format(price))
        print('등록월 : {}'.format(date))
        print('상품의견 : {}건'.format(review))
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