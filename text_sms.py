from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Textnow:  

        def __init__(self, TN_USER, TN_PASS, PHONE_NUMBER, MESSAGE):
                self.TN_USER = TN_USER
                self.TN_PASS = TN_PASS
                self.PHONE_NUMBER = PHONE_NUMBER
                self.MESSAGE = MESSAGE
                self.url = "https://www.textnow.com/login"

        def send_text(self):
                options = webdriver.ChromeOptions()
                            
                options.add_argument("-headless")
                #driver = webdriver.Chrome(chrome_options=options)
                driver = webdriver.Chrome()
                try:
                        driver.get(self.url)
                except:
                        pass
                time.sleep(8)
                print('OK')

                WebDriverWait(driver, 8).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
                uname_box = driver.find_element_by_xpath("//input[@name='username']")
                pass_box = driver.find_element_by_xpath("//input[@name='password']")
                uname_box.send_keys(self.TN_USER)
                pass_box.send_keys(self.TN_PASS)

                login_btn = driver.find_element_by_xpath("//button[@type='submit']")
                login_btn.click()

                try:
                        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@class='form_button']")))
                except:
                       pass

                got_it = driver.find_element_by_xpath("//input[@class='form_button']")
                got_it.click()

                new_text_btn = driver.find_element_by_xpath("//button[@id='newText']")
                new_text_btn.click()

                number_field = driver.find_element_by_xpath("//input[@class='newConversationTextField']")
                number_field.send_keys(self.PHONE_NUMBER)

                text_field = driver.find_element_by_xpath("//textarea[@id='message']")
                text_field.click()
                text_field.send_keys(self.MESSAGE)

                send_btn = driver.find_element_by_xpath("//div[@class='send-btn']")
                send_btn.click()
