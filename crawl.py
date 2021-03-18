# coding: utf-8
from time import sleep

from selenium import webdriver
# from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 1.Khai bao bien browser
options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches',
    ['enable-logging'],
)
browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# 2. Mo thu 1 trang web
browser.get("https://docs.google.com/forms/d/e/1FAIpQLScCjE2391bq8jrF1h74IxrD8OsMpXRy8Z9n0gmof1euL_85AA/viewanalytics?fbclid=IwAR3ID5tMSaDzSDyN8NBiyqHd2_YgCuu-11vSjtCsWRSjTzzS-ESUSKB139M")
sleep(10)

# 3.Tim du lieu
name_list = browser.find_elements_by_class_name("freebirdCommonAnalyticsTextResponse freebirdLightBackground")
sleep(5)
for name in name_list:
    print(name)
sleep(5)
input('Nhập enter')
# 4. Dong trang web
browser.close()
