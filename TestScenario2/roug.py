from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\\Users\\Srinivas\\PycharmProjects\\SeleniumPython101\\Driver\\chromedriver.exe")
driver.get("https://www.lambdatest.com/selenium-playground/")

driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Drag & Drop Sliders']").click()
# driver.find_element(By.XPATH,"//input[@value='15']").click()
# driver.find_element(By.XPATH,"//output[@id='rangeSuccess']").send_keys("95")
#
# drag_ten = driver.find_element(By.XPATH,"//input[@value=15]")
# drop_eighty = driver.find_element(By.XPATH,"//input[@value=90]")
# ActionChains(driver).drag_and_drop_by_offset(drag_ten, drop_eighty).perform()

slider = driver.find_element(By.XPATH,'//input[@value=15]')
slide = ActionChains(driver).drag_and_drop_by_offset(slider, 105, 0).perform()

()#-m pytest -n 3 C:\test_file.py --html=C:\Report.html)
# pytest -n 3 --html==report.html



# source1 = driver.find_element(By.XPATH,"//output[@id='rangeSuccess']")
# action = ActionChains(driver)
# action.drag_and_drop_by_offset(source1, 100, 100).perform()

# driver.find_element(By.XPATH,"//input[@id='user-message']").send_keys("Welcome To Lambda Test")
# driver.find_element(By.XPATH,"//button[@id='showInput']").click()
# rough = driver.find_element(By.XPATH,"//p[@id='message']").text
# assert ("Welcome To Lambda Test" in rough)
# print(rough)
