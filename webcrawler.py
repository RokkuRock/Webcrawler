# Import Selenium Modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Specify path of Chrome Driver
options= Options()
options.chrome_executable_path="D:\repoProjects\web-crawler\chromedriver.exe"
# Create Driver object entity for manipulating browser actions
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.google.com")
driver.save_screenshot("google.png")
driver.get("https://www.ntu.edu.tw")
driver.save_screenshot("ntu.png")
driver.close()
