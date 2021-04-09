#!/usr/local/bin/python3
import datetime
from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def main(driver: webdriver):
    """
    Googleで検索を実行する
    :param browser: webdriver
    """
    # スクリーンショットのファイル名用に日付を取得
    dt = datetime.datetime.today()
    dtstr = dt.strftime("%Y%m%d%H%M%S")

    # Googleにアクセス
    driver.get('https://www.google.co.jp/')
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)

   # キーワードの入力
    search_box = driver.find_element_by_name("q")
    search_box.send_keys('docker selenium')

    # 検索実行
    search_box.submit()
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)

    # スクリーンショット
    driver.save_screenshot('images/' + dtstr + '.png')

if __name__ == '__main__':
    try:
        #browser = webdriver.Firefox()  # 普通のFilefoxを制御する場合
        #browser = webdriver.Chrome()   # 普通のChromeを制御する場合

        # HEADLESSブラウザに接続
        browser = webdriver.Remote(
            command_executor='http://chrome:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)

        # Googleで検索実行
        main(browser)

    finally:
        # 終了
        browser.close()
        browser.quit()

