from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


test_url = "https://www.python.org"
test_url_2 = "https://en.wikipedia.org/wiki/Main_Page"

# to keep the browser window open after the end of the program:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=test_url)

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)


driver.get(test_url_2)
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
article_count.click()

pages = driver.find_element(By.LINK_TEXT, value="Pages")
pages.click()

search_box = driver.find_element(By.NAME, value="search")
search_box.send_keys("Python")
search_box.send_keys(Keys.ENTER)

python_programming_link = driver.find_element(By.XPATH, value="//a[@title='Python (programming language)']")
python_programming_link.click()


# driver.close()
# driver.quit()