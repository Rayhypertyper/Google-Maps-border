from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fuzzywuzzy import fuzz

# url = "https://bwt.cbp.gov/details/04070801/POV"
def navigate_website(border_name):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Optional, improves stability on some systems
    chrome_options.add_argument('--log-level=3')  # Suppresses most logs
 
    service = Service(executable_path="chromedriver.exe")
    service.arguments = ["--log-level=3"]
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigates to dropdown menu to reveal it in html
    driver.get("https://bwt.cbp.gov/")
    dropdown_button = driver.find_element(By.CLASS_NAME, "dropdown-toggle")  # Update the class if needed
    dropdown_button.click()

    # Finds names of all possible border crossings on website
    dropdown_menu = driver.find_element(By.CLASS_NAME, "dropdown-menu")
    menu_items = dropdown_menu.find_elements(By.TAG_NAME, "li")
    links = dropdown_menu.find_elements(By.TAG_NAME, "a")
    urls = {}

    # Adds borders and their url to a dictionary
    for i in range(len(menu_items)):
        urls[menu_items[i].text] = links[i].get_attribute("href")

    # Checks which border name is closest to input and returns link for given border
    for i in urls:
        token_set_ratio = fuzz.token_set_ratio(border_name, i)
        if token_set_ratio > 70:
            link = urls[i]
            return link, i
    return None


    