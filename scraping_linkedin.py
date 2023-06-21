from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def scrape_linkedin(linkedin_email, linkedin_password):

    driver = webdriver.Chrome()  # driver for Chrome browser
    driver.get("https://www.linkedin.com/login") # Opening LinkedIn login page

    # Entering LinkedIn credentials in the browser
    driver.find_element(By.ID,"username").send_keys(linkedin_email)
    driver.find_element(By.ID,"password").send_keys(linkedin_password)
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    time.sleep(2)

    # Scraping the number of unread messages and notifications
    unread_messages = driver.find_element(By.XPATH,"/html/body/div[5]/header/div/nav/ul/li[4]/a/div/span/span[1]").text
    print("number of unread Messages: ",unread_messages)

    unread_notifications = driver.find_element(By.XPATH,"/html/body/div[5]/header/div/nav/ul/li[5]/a/div/span/span[1]").text
    print("number of unread notifications",unread_notifications)

    # Quit the browser
    driver.quit()
    return [unread_messages,unread_notifications]