from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser=webdriver.Chrome()

browser.get("http://suninjuly.github.io/alert_accept.html")
button1=browser.find_element_by_css_selector(".btn.btn-primary")
button1.click()
confirm=browser.switch_to.alert
confirm.accept()
value=browser.find_element_by_css_selector("span#input_value.nowrap").text
input1=browser.find_element_by_id("answer")
y=calc(value)
input1.send_keys(y)
button2=browser.find_element_by_css_selector(".btn.btn-primary")
button2.click()
