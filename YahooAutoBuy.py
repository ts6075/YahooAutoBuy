# coding=utf8
# #################
# 作者: Nick
# 開始日期: 20210312
# 程式目的: Yahoo商城下單程式
# #################
import configparser            # 解析config
from selenium import webdriver
import time


# #################
# # 基礎設定       #
# #################
config = configparser.ConfigParser()
config.read('Config.ini')
loginUrl = 'https://login.yahoo.com/?.done=https%3A%2F%2Ftw.dictionary.search.yahoo.com'
username = config.get('Section_Info', 'loginEmail')         # 會員帳號
password = config.get('Section_Info', 'password')           # 會員密碼
commodityUrl = config.get('Section_Info', 'commodityUrl')   # 商品Url
buyCount = int(config.get('Section_Info', 'buyCount')) - 1  # 購買數量,預設已經是一筆,故要減1

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
# 如商品處於開放購買倒數,則會進入迴圈,直到開放時自動進入購買程序
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

# 購買數量調整
print('#################')
print('# 購買數量調整中...       #')
for i in range(buyCount):
    driver.find_element_by_class_name('hRJnbB').click()
print('# 購買數量已追加' + str(buyCount) + '個       #')

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
