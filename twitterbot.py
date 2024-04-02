if True:
    username = 'Whitewo36928561'
    password = 'Abhi@962212'
    link = 'https://twitter.com/compose/tweet'
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
if True:

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(options = chrome_options)

    driver.get(link)


# LOGIN
# Username Enter
time.sleep(2)
user = driver.find_element(By.NAME, 'text')
user.send_keys(username)

next = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
next.click()

# password screen
time.sleep(2)
entering_password = driver.find_element(By.NAME, 'password')
entering_password.send_keys(password)

Login = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
Login.click()

# Selecting media
time.sleep(5)
tweet_path = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div[1]'
media = driver.find_element(By.XPATH, tweet_path).send_keys('I love Old architectures')

time.sleep(2)
upload_image_path = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div[2]/div'
driver.find_element(By.XPATH, upload_image_path).send_keys("F:\stuff\23rd jan 2022\IMG_3342.jpg")

