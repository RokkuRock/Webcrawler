import subprocess
import sys

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'openpyxl'])

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl

options = webdriver.ChromeOptions()
options.add_argument('--disable-web-security')
options.add_argument('--disable-features=IsolateOrigins,site-per-process')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.123 Safari/537.36')
driver = webdriver.Chrome(options=options)

url = "https://www.timeshighereducation.com/world-university-rankings/2022/reputation-ranking#!/page/0/length/100/sort_by/rank/sort_order/asc/cols/stats"
driver.get(url)

try:
    wb = openpyxl.Workbook()
    ws = wb.active

    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        row_data = []
        for col in cols:
            row_data.append(col.text)
        ws.append(row_data)

    # Adding column headers
    column_headers = ["Rank", "Institution", "Country", "Reputation Score"]
    ws.insert_rows(1)
    for col_num, header in enumerate(column_headers, 1):
        cell = ws.cell(row=1, column=col_num)
        cell.value = header

    # Save the workbook
    wb.save('university_rankings.xlsx')

finally:
    driver.quit()
