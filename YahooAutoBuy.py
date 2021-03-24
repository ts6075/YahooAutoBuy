# coding=utf8
# #################
# 作者: Nick
# 開始日期: 20210312
# 程式目的: Yahoo商城下單程式
# 版本記錄
# v1.0 - 20210312 - 初版
# #################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# #################
# # 基礎設定       #
# #################
loginUrl = 'https://login.yahoo.com/?.done=https%3A%2F%2Ftw.dictionary.search.yahoo.com'
username = 'xxxxx'
password = 'xxxxxxxxxx'
# commodityUrl = 'https://tw.buy.yahoo.com/gdsale/gdsale.asp?gdid=8378928'
commodityUrl = 'https://tw.buy.yahoo.com/gdsale/gdsale.asp?gdid=9352727'

print('#################')
print('# 啟動中...     #')
driver = webdriver.Chrome('./chromedriver')                 # 啟動Chrome
driver.implicitly_wait(10)


# #################
# # 登入作業       #
# #################
driver.get(loginUrl)                                        # 載入登入頁面
print('#################')
print('#################')
print('# 登入中...     #')
driver.find_element_by_id('login-username').send_keys(username)
driver.find_element_by_id('login-signin').click()
driver.implicitly_wait(10)
driver.find_element_by_id('login-passwd').send_keys(password)
driver.find_element_by_id('login-signin').click()
driver.implicitly_wait(3)
print('# 登入成功      #')
print('#################')

# #################
# # 商品購買       #
# #################
i = 1
print('#################')
while(True):
    try:
        print('第', i, '次載入商品頁面')
        driver.get(commodityUrl)                                    # 載入商品頁面
        driver.implicitly_wait(3)
        print(driver.find_element_by_class_name('CheckoutBar__wrapper___1spVa')
                    .find_element_by_class_name('CheckoutBar__buyNowBtn___qgDtR')
                    .click())
        break
    except Exception as ex:
        print(ex)
        print('trying...')
        i = i + 1
        time.sleep(0.5)
print('#################')

# 購買數量增加一個(共2個)
print('#################')
print('# 購買數量調整中...       #')
driver.find_element_by_class_name('hRJnbB').click()
print('# 購買數量已增加一個      #')

# 點擊確認購買按鈕(進入付款階段)
print('# 嘗試點擊確認購買按鈕... #')
# js = "document.getElementsByClassName('submitButton')[0].click();"
# driver.execute_script(js)
time.sleep(1)
driver.find_elements_by_class_name('submitButton')[1].click()
print('# 已點擊確認購買按鈕      #')
print('# 載入付款設定頁面中...   #')
driver.implicitly_wait(3)
print('# 已成功進入付款階段      #')
print('#################')

# 取消訂閱電子報(預設是訂閱)
try:
    print('#################')
    print('# 取消訂閱電子報中...     #')
    driver.find_element_by_class_name('jForQE').click()
    print('# 已取消訂閱電子報        #')
except Exception as ex:
    print(ex)
    print('# 取消訂閱電子報失敗      #')
    time.sleep(0.5)

# 點擊完成購買按鈕
i = 1
while(True):
    try:
        print('# 嘗試點擊完成購買按鈕... #')
        driver.find_element_by_class_name('submitButton').click()
        print('# 已點擊完成購買按鈕      #')
        break
    except Exception as ex:
        print(ex)
        print('trying...', i)
        i = i + 1
        time.sleep(0.5)

# 最後確認購買按鈕
i = 1
while(True):
    try:
        print('# 嘗試點擊最後確認購買按鈕... #')
        js = "document.getElementsByName('confirm')[0].click();"
        driver.execute_script(js)
        print('# 已點擊最後確認購買按鈕      #')
        driver.implicitly_wait(10)
        break
    except Exception as ex:
        print(ex)
        print('trying...', i)
        i = i + 1
        time.sleep(0.5)

print('#################')
print('#################')
print('# 已完成下單     #')
print('#################')
# driver.close()                                              # 關閉Chrome
# driver.quit()
