from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Scrape the links, addresses, and prices of the rental properties

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Use our Zillow-Clone website (instead of Zillow.com)
response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

# Create a list of all the links on the page using a CSS Selector
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [
    link["href"]
    for link
    in all_link_elements
]

# Create a list of all the addresses on the page using a CSS Selector (remove newlines \n, pipe symbols |, and whitespaces to clean up the address data)
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [
    address.get_text().replace(" | ", " ").strip()
    for address
    in all_address_elements
]

# Create a list of all the prices on the page using a CSS Selector (get a clean dollar price and strip off any "+" symbols and "per month" /mo abbreviation)
all_price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [
    price.get_text().replace("/mo", "").split("+")[0]
    for price
    in all_price_elements
    if "$" in price.text
]

# Fill in the Google Form using Selenium
# Use the xpath to select the "short answer" fields in your Google Form (your xpath might be different if you created a different form)
google_form_link = "YOUR_GOOGLE_FORM_LINK_HERE"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # keep browser window open
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    driver.get(google_form_link)
    time.sleep(2)

    address = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()