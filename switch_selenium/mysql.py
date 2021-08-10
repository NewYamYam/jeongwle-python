# import pymysql

# conn = pymysql.connect(
#     user = "jeongwle",
#     passwd = "1q2w3E4R!",
#     host = "localhost",
#     db = "NINTENDO"
# )
# cursor=conn.cursor()
# string = "http://prod.danawa.com/info/?pcode=11215266&cate=11338057"
# a = 0
# result = cursor.execute("SELECT * FROM switchtitle WHERE link = '%s" %string)
# # result = cursor.execute("CREATE TABLE test5 (number int)")
# print(result)
# # cursor.execute("CREATE TABLE switchtitle (number int, title text, price text, date text, 'review' text)")
# # idx = 0
# # i = 1
# # for j in range(total):
# #     cursor.execute(
# #         f'INSERT INTO switchtitle VALUES({i}, \"{results[idx][0]}\", \"{results[idx][1]}\", \"{results[idx][2]}\", \"{results[idx][3]}\")'
# #     )
# #     i += 1
# #     idx += 1
# conn.commit()
# conn.close()

#### , 빼는거 고민####
b = "1,234"
a =int(b.replace(',', ""))
print(b + '-')
# from selenium import webdriver
# import chromedriver_autoinstaller
# import time

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('ignore-certificate-errors')
# try:
#     driver = webdriver.Chrome("/Users/jeongwle/Downloads/chromedriver", options=options)
#     # driver = webdriver.Chrome("/Users/jeongwle/Downloads/chromedriver")
# except:
#     path = chromedriver_autoinstaller.install()
#     driver = webdriver.Chrome(path, options=options)

# driver.implicitly_wait(10)
# driver.get(url='http://prod.danawa.com/list/?cate=11338057')
# total = int(driver.find_element_by_css_selector(
#     '#danawa_content > div.product_list_wrap > div > div.prod_list_tab > ul > li.tab_item.selected > a > strong.list_num').text.strip('()'))
# idx = 0
# price = list(range(0, total))
# li_list = driver.find_elements_by_css_selector(
#     '#productListArea > div.main_prodlist.main_prodlist_list > ul > li.prod_item.prod_layer[id]') #[id]는 li.prod_item.prod_layer중 id를 가진애들만 한다는 뜻
# for product in li_list:
#     price[idx] = product.find_element_by_css_selector('div > div.prod_pricelist > ul > li > p.price_sect > a > strong').text
# print(int(price[0].replace(',',"")))

# a =list(range(0,4))
# a[0] = 1
# a[1] = 'hi'
# a[2] = 3
# a[3] = "bye"
# print(a)