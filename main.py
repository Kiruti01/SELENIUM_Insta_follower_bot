from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "samdoesarts"
USERNAME = "USERNAME"
PASSWORD = "*****"
INSTA_URL = "https://www.instagram.com/accounts/login/"

s = Service(CHROME_DRIVER_PATH)
# driver = webdriver.Chrome(service=s)

class InstaFollower:
    def __init__(self, driver):
        self.driver = webdriver.Chrome(service=s)
        time.sleep(5)

    def login(self):
        self.driver.get(INSTA_URL.encode("ascii", "ignore").decode("unicode_escape"))
        time.sleep(5)
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        not_now_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_button.click()
        #
        # # time.sleep(7)
        # # not_now_button_two = self.driver.find_element(By.CLASS_NAME, '_a9-- _a9_1')
        # # not_now_button_two.click()
        # time.sleep(7)
        # no_notifications = self.driver.find_element(By.CSS_SELECTOR, '._a9-- _a9_1')
        # no_notifications.click()

        ui.WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Not Now')]"))).click()
        # acpt = self.driver.find_element(By.XPATH,  "//*[contains(@class, '_a9-- _a9_1')]")
        # acpt.click()

    def find_followers(self):
        time.sleep(2)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(5)
        followers = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div')
        followers.click()

        time.sleep(5)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)



    def follow(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
        for button in buttons:
            if button.text != "Follow":
                pass
            else:
                self.driver.execute_script("arguments[0].click();", button)
                time.sleep(2)

        # get_followers = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        # for button in get_followers:
        #     num = 0
        #     while num < len(get_followers):
        #         while num < len(get_followers):
        #             print(len(get_followers))
        #             follower = get_followers[num]
        #             while get_followers[num].text == "Follow":
        #         # Sometimes clicking Follow didn't do anything.
        #         # Repeat click until it works
        #         # Added the try block for if/when following another user has users
        #         # I'm already following previously in it.
        #                 try:
        #                     button.click()
        #                     time.sleep(2)
        #                 except ElementClickInterceptedException and StaleElementReferenceException:
        #                     cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
        #                     cancel_button.click()
        #
        #                 time.sleep(3)
        #                 get_followers = self.driver.find_element(By.CSS_SELECTOR, "li button")
        #             num += 1


        # pass



bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
