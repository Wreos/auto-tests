from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")
x_element=browser.find_element_by_id("input_value")
x=x_element.text
y=calc(x)
search_form=browser.find_element_by_id("answer")
search_form.send_keys(y)
checkbox=browser.find_element_by_id("robotCheckbox")
checkbox.click()
radiobutton=browser.find_element_by_id("robotsRule")
radiobutton.click()
send=browser.find_element_by_css_selector("button.btn.btn-default")
send.click()