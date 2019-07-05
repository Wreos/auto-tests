from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math


browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")
n1=browser.find_element_by_id("num1").text
n2=browser.find_element_by_id("num2").text
sum=(int(n1)+int(n2))
select=Select(browser.find_element_by_id("dropdown"))
select.select_by_value(str(sum))
send=browser.find_element_by_css_selector("button.btn.btn-default")
send.click()