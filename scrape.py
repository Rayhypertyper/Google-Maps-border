
from playwright.sync_api import sync_playwright
import time
def find_wait_times(url, time_at_border):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        # Clicks the "Table" tab
        page.locator("text=Table").click()
        html = page.content()
        
        # Wait for the table to load
        page.wait_for_selector("#sectionB")
        time.sleep(5)
        td_elements = page.locator("tbody td").all_inner_texts()
        # print(td_elements)  

    # Iterates and extracts scraped data
    for i in range(len(td_elements)):
        if str(td_elements[i]) == str(time_at_border):
            border_wait = td_elements[i+2]
            return border_wait


            