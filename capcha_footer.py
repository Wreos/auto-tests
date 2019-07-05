from selenium import webdriver
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

x_element=browser.find_element_by_id("input_value")
x=x_element.text
y=calc(x)

textbox=browser.find_element_by_id("answer")
textbox.send_keys(y)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
checkbox=browser.find_element_by_id("robotCheckbox")
checkbox.click()
radiobutton=browser.find_element_by_id("robotsRule")
radiobutton.click()
button.click()
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))