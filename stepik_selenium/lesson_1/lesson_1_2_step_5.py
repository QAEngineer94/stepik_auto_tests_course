import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
print(fun(5))
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")
