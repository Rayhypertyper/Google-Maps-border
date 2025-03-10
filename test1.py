from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

from playwright.sync_api import sync_playwright
url = "https://bwt.cbp.gov/details/04070801/POV"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    # browser = p.chromium.launch(headless=False)  # Set headless=True if you don't want UI
    # page = browser.new_page()

    # Open the page
    page.goto("https://bwt.cbp.gov/details/04070801/POV")

    # Wait for and click the "Table" tab
    page.locator("text=Table").click()
    html = page.content()
    # print(html)
    # Wait for the table to load
    page.wait_for_selector("#sectionB")
    time.sleep(3)
    print('hi')
    td_elements = page.locator("tbody td").all_inner_texts()
    print(td_elements)  
    
    time.sleep(1000)

    # Wait for JavaScript to load
    # page.wait_for_selector(".nav")

    # Wait for the link with text "Table" to be present
    # page.wait_for_selector("a:has-text('Table')")

    # Click the "Table" link
    # table_tab = page.query_selector("a:has-text('Table')")
    # table_tab.click()
    
    # page.locator("text=Table").click()
    # table = page.wait_for_selector("#sectionB")
    # print(table)
    # Get fully rendered HTML
    # html = page.content()

    

# Parse with BeautifulSoup
# soup = BeautifulSoup(html, "html.parser")

# # Find and print the table
# table = soup.find("table", class_="table")
# print(table)
'''
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=True)
#     page = browser.new_page()
#     page.goto(url)
#     print(page.title())
#     browser.close()
# session = HTMLSession()
# response = session.get(url)
# response.html.render()
# # soup = BeautifulSoup(response.content, 'html.parser')

# # print(soup.find_all('table', class_='table'))

# print(response.html)
# print(response.html.html)





driver.get(url)

# element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "nav"))
#     )
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.LINK_TEXT, "Table"))
#     )  # Wait for the tab list


table_tab = driver.find_element(By.LINK_TEXT, "Table")
table_tab.click()
# driver.execute_script("arguments[0].click();", table_tab)

  # Update the class if needed
# print(dropdown_button)
# dropdown_button.click()




table = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "sectionB"))
)
time.sleep(10)
tbody = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "tbody"))
)
print(tbody.text)
time.sleep(1000)
# tdody = table.find_element(By.XPATH, "//td[text()='11:00 PM']")
# print(tdody.text)

# )
# driver.find_element(By.TAG_NAME, "tbody")
# print("Found tbody:", tbody)
# print("Tbody is displayed:", tbody.is_displayed())
# print("Tbody text:", tbody.text)

# rows = tbody.find_elements(By.TAG_NAME, "tr")
# print("Number of rows found:", len(rows))
# for row in rows:
#     print("Row text:", row.text)
# print(table.text)
# print('hi')
# try:
#     a = WebDriverWait(table, 10).until(
#         EC.presence_of_element_located((By.TAG_NAME, "tbody"))
#     )
# except:
#     print('nah')
# rows = table.find_element(By.TAG_NAME, "tbody")
                          
# print(a.is_displayed())
# time.sleep(13) 
# print(rows.is_displayed())
# for row in rows:
    # print(row.text)
# Extract times (first column of each row)
# times = [row.find_element(By.XPATH, "./td[1]").text for row in rows]

# Print extracted times
# print(times)
# tr = table.find_elements(By.CLASS_NAME, "table")
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))
# rows = driver.find_elements(By.TAG_NAME, "Tbody")
# Locate the table
# table = driver.find_elements(By.CLASS_NAME, "table")

# Find all rows in the table body
# for t in table:
#     print(t.text)

# Extract the times from the first column

# for i in range(len(tr)):
#     if tr[i] == "10:00 AM":
#         border_wait = tr[i+2]
#         print(border_wait)
'''