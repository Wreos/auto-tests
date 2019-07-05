from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

options = webdriver.ChromeOptions()
options.add_experimental_option('w3c', False)

browser = webdriver.Chrome(chrome_options=options)
# говорим WebDriver ждать все элементы в течение 5 секунд

browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000"))
button= browser.find_element_by_id("book")
button.click()

value=browser.find_element_by_css_selector("span#input_value.nowrap").text
input1=browser.find_element_by_id("answer")
y=calc(value)
input1.send_keys(y)
button2=browser.find_element_by_id("solve")
button2.click()

