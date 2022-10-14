
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service

driver = webdriver.Chrome(executable_path="C:\\Users\\Srinivas\\PycharmProjects\\SeleniumPython101\\Driver\\chromedriver.exe")
driver.get("https://www.lambdatest.com/selenium-playground/")

driver.maximize_window()
driver.find_element(By.XPATH, "//a[normalize-space()='Input Form Submit']").click()
result = driver.find_element(By.XPATH, "//input[@id='name']")
driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
res = result.get_attribute("validationMessage")
assert "Please fill out this field." in res
print(res)


# driver.find_element(By.XPATH,"//a[normalize-space()='Simple Form Demo']").click()
# driver.find_element(By.XPATH,"//input[@id='user-message']").send_keys("Welcome To Lambda Test")
# driver.find_element(By.XPATH,"//button[@id='showInput']").click()
# rough = driver.find_element(By.XPATH,"//p[@id='message']").text
# assert ("Welcome To Lambda Test" in rough)
# print(rough)
