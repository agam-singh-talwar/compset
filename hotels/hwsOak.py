import pprint
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Setup Selenium WebDriver (you may need to install geckodriver for Firefox or chromedriver for Chrome)
# Adjust the path as needed
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://www.hilton.com/en/book/reservation/rooms/?ctyhocn=YYZOVHW&arrivalDate=2024-07-03&departureDate=2024-07-04&aaaRate=false&aarpRate=false&corporateCode=&employeeRate=false&friendsAndFamilyRate=false&fromId=&governmentRate=false&groupCode=&offerId=&ownerHGVRate=false&ownerVIPRate=false&pnd=&promotionCode=&redeemPts=false&seniorRate=false&smbRate=false&travelAgent=false&travelAgentId=&room1NumAdults=1")

# Wait for the page to load (adjust the sleep duration as needed)
time.sleep(3)  # reduced to 3

# Get the page source
html = driver.page_source

# Now parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Attempt to find the div elements again
rates = soup.find_all('button', {
    'class': 'block w-full px-1 font-extrabold sm:text-lg bg-primary text-bg hover:bg-primary-alt rounded-md py-3'})

pprint.pprint(rates)


def checkForAvailability_KSTN(rates):
    roomMoreRatesButtonKSTN_present = any(
        'roomMoreRatesButtonKSTN' in rate.get('data-cypress', '') for rate in rates)
    return roomMoreRatesButtonKSTN_present


def checkForAvailability_KHWN(rates):
    roomMoreRatesButtonKHWN_present = any(
        'roomMoreRatesButtonKHWN' in rate.get('data-cypress', '') for rate in rates)
    return roomMoreRatesButtonKHWN_present


def GetRateKHWN(rates, checkForAvailability_KHWN):
    if checkForAvailability_KHWN(rates):
        # Wait until the button is clickable, and click it
        wait = WebDriverWait(driver, 10)
        btn = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[data-cypress='roomMoreRatesButtonKHWN']")))

        btn.click()

        # Get the current page URL after clicking the button
        nextPage = driver.current_url

        print(nextPage)
    else:
        return None


GetRateKHWN(rates, checkForAvailability_KHWN)
# Don't forget to close the driver
driver.quit()
