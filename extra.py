from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = 'Whitewo36928561'
password = 'Abhi@962212'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# PROMISED_DOWN = 150
# PROMISED_UP = 10

PROMISED_DOWN = int(input("Type in the Download speed promised: "))
PROMISED_UP = int(input("Type in the Upload speed promised: "))

speed_test_link = 'https://www.speedtest.net/'
twitter_link = 'https://twitter.com/compose/tweet'


class internet_speed_bot:
    def __init__(self):
        self.browser = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        print()
        print("The Internet Speed is being Calculated, wait for 60 seconds...")
        print()

        self.browser.get(speed_test_link)
        time.sleep(5)
        self.cookie = self.browser.find_element(By.CSS_SELECTOR, '#onetrust-accept-btn-handler')
        self.cookie.click()

        time.sleep(1)
        self.button = self.browser.find_element(By.CSS_SELECTOR, '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.start-button > a > span.start-text')
        self.button.click()

        # Calculating
        time.sleep(60)

        self.download_speed = self.browser.find_element(By.CLASS_NAME, 'download-speed').text
        self.upload_speed = self.browser.find_element(By.CLASS_NAME, 'upload-speed').text
        self.provider = self.browser.find_element(By.CLASS_NAME, 'js-data-isp').text

        self.data = [self.download_speed, self.upload_speed, self.provider]
        # print(self.data)
        print(f"Your current Download speed is {self.download_speed} and current Upload speed is {self.upload_speed}")
        if float(self.data[0]) <= float(PROMISED_DOWN):
            print(f"Since the Download speed is not upto the mark, we'll complain from your side to the internet provider on twitter. ")
        else:
            print(f"Since the Download speed is upto the mark, So we'll send a good word and appreciate their work through Twitter :). ")

        print()
        return self.data

    def tweet_at_provider(self, data):
        print("Wait for sometime, the Tweet is being poster through your id. ")
        self.browser.get(twitter_link)
        time.sleep(5)
        # time.sleep(20)
        user = self.browser.find_element(By.NAME, 'text')
        user.send_keys(username)

        next = self.browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next.click()

        # password screen
        time.sleep(3)
        # time.sleep(10)
        entering_password = self.browser.find_element(By.NAME, 'password')
        entering_password.send_keys(password)

        Login = self.browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        Login.click()

        # Writing
        time.sleep(10)
        # time.sleep(20)
        tweet_path = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div'
        # tweet_path = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div[1]'
        if float(data[0]) > float(PROMISED_DOWN):
            self.browser.find_element(By.XPATH, tweet_path).send_keys(f'Dear @{data[2]} Internet provider, The internet speed that I was promised was 75Mbps, and I am getting {data[0]} UP / {data[1]} DOWN, which is plenty, thankyou, We appreciate your service and keep up the good work, thankyou.')
        else:
            self.browser.find_element(By.XPATH, tweet_path).send_keys(f'Dear @{data[2]} Internet provider, The internet speed that I was promised was 75Mbps, but the speed Im getting currently at this moment is {data[0]} UP /{data[1]} DOWN, which is not  upto the mark, please take a look at this and I hope to recieve what I was promised. Thankyou')

        post = self.browser.find_element(By.CSS_SELECTOR, '#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1habvwh.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-rsyp9y.r-1pjcn9w.r-htvplk.r-1udh08x.r-1potc6q > div > div > div > div:nth-child(3) > div.css-1dbjc4n.r-kemksi.r-1pp923h.r-1moyyf3.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-kemksi.r-jumn1c.r-xd6kpl.r-gtdqiz.r-ipm5af.r-184en5c > div:nth-child(2) > div > div > div:nth-child(2) > div.css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr')
        post.click()

# //*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div