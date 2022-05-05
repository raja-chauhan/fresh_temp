from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox(executable_path="./geckodriver")
driver.maximize_window() # For maximizing window
driver.implicitly_wait(1000) # gives an implicit wait for 20 seconds
# driver.get('https://www.linuxhint.com')
# print('Title: %s' % driver.title)
# driver.quit()
driver.get('https://app.uniswap.org/#/pool/228251?chain=mainnet')
time.sleep(10)
# eth1 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[4]/div/div[2]/div[2]/div[1]/div/div[1]/div[2]")
eth1 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[4]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]")
usdt1 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[4]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[2]/div/div[1]")
print('eth1 -->',eth1.text)
print('usdt1 -->',usdt1.text)
eth2 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[4]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div")
usdt2 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[4]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div")
print('eth2 -->',eth2.get_attribute('innerHTML'))
print('usdt2 -->',usdt2.get_attribute('innerHTML'))