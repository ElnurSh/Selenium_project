from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

service = Service('/Users/User/Downloads/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)

driver.get('https://www.e-pul.az/epay/ru/category/mobile/nar')
select = Select(driver.find_element('name', 'selPref'))
select.select_by_visible_text('077')
p_number = driver.find_element('name', 'phone')
p_number.send_keys("6020060")
click_button1 = driver.find_element('xpath', '//*[@id="tab_157_0"]/form/div[3]/div/input')
click_button1.click()
pay = driver.find_element('id', 'amount')

pay.send_keys("5")

click_button2 = driver.find_element('xpath', '/html/body/section[2]/div/div/div[1]/div[2]/div/div[2]/div/div[2]')
click_button2.click()
print(driver.current_url)

#driver.quit()