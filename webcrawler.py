# Import Selenium Modules
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
import time
# Specify path of Chrome Driver
options= Options()
options.chrome_executable_path="D:\repoProjects\web-crawler\chromedriver.exe"
# Create Driver object entity for manipulating browser actions
driver=webdriver.Chrome(options=options)
# Link to the target website URL
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
# Get the original html of the page
tags=driver.find_elements(By.CLASS_NAME, "title") # search for all text of title class property
for tag in tags:
    print(tag.text)
# Return to last page for more titles
link=driver.find_element(By.LINK_TEXT, "‹ 上頁")
link.click() #simulation of mouse-clicking event
time.sleep(3) #waiting for rendering
# crawling titles one more time
tags=driver.find_elements(By.CLASS_NAME, "title") # search for all text of title class property
for tag in tags:
    print(tag.text)
driver.close()


