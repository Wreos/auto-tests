from selenium import webdriver
import math
import os


browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")
input1=browser.find_element_by_name("firstname")
input1.send_keys("Alex")

input2=browser.find_element_by_name("lastname")
input2.send_keys("Lozhkovoi")

input3=browser.find_element_by_name("email")
input3.send_keys("21321312")

upload=browser.find_element_by_id("file")

curr_dir=os.path.abspath(os.path.dirname(__file__))
file_path=os.path.join(curr_dir,'file.txt')
upload.send_keys(file_path)
send=browser.find_element_by_css_selector("button.btn.btn-primary")
send.click()