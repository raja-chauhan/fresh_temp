from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="./geckodriver")
# driver.get('https://www.linuxhint.com')
# print('Title: %s' % driver.title)
# driver.quit()

driver.get('https://youtube.com')

searchbox = driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
# //*[@id="search"]
# searchbox = driver.find_element_by_xpath('//*[@id="container"]')
driver.implicitly_wait(10)
time.sleep(10)
print("Element is visible? " + str(searchbox.is_displayed()))


searchbox.send_keys("Raja chauhan")

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()