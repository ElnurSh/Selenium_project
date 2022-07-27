from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

service = Service('/Users/User/Downloads/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)

driver.get('https://www.e-pul.az/epay/ru/category/mobile/nar')
select = Select(driver.find_element('name', 'selPref'))
select.select_by_visible_text('077')
item = driver.find_element('name', 'phone')
item.send_keys("6020060")
#driver.quit()