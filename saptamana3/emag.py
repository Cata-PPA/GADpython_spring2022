import time
from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException


browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.emag.ro/#opensearch")
get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
get_element.send_keys(('telefon'))
get_element.submit()
time.sleep(10)


browser.close()