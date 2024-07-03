import pprint
import time
from selenium import webdriver
from bs4 import BeautifulSoup

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

# Don't forget to close the driver
driver.quit()
