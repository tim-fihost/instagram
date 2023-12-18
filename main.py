from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time
LINK = 'https://www.instagram.com/'
USER = 'Your User Name'
PW = 'PASSWORD'
FOLLOWERS = 'jennierubyjane'
class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(LINK)

    def login(self):
        user_input = self.driver.find_element(By.NAME, value='username')
        user_input.send_keys(USER)
        pw_input = self.driver.find_element(By.NAME, value='password')
        pw_input.send_keys(PW)
        time.sleep(5)
        login_in_button = self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[3]/button')
        login_in_button.click()
        time.sleep(5)
        #Only this step sometimes may requrie actually human intreaction with clicking
        #Since tags are given dynamiclly
        try:
            not_now = self.driver.find_element(By.XPATH, value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
            not_now.click()
        except NoSuchElementException:
            print("No such element do it manually")
            time.sleep(3)
        time.sleep(4)
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()
        print("NEXT")
        
    def find_followers(self,account_name):
        time.sleep(2)
        self.driver.get(f"https://www.instagram.com/{account_name}/followers")'
        time.sleep(5)
        people = '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]'
        #"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]"
        modal = self.driver.find_element(by=By.XPATH, value=people)
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
        time.sleep(3)
        
    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required.
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

jennie = InstaFollower()
jennie.login()
for i in range(10):
    jennie.find_followers(FOLLOWERS)
    jennie.follow()
time.sleep(1000)
