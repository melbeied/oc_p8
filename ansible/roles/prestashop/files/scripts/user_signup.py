
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import configparser
config = configparser.ConfigParser()
config.read('./config.ini')
if not os.path.exists('./user_signup'):
    os.makedirs('./user_signup')

options = Options()
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')
driver.get(config['common']['signup_url'].strip())

WebDriverWait(driver, 30);
driver.get_screenshot_as_file("user_signup/01_startScreen.png")



gender = config['signup']['gender'].strip()

driver.find_elements_by_xpath("//input[@type='radio' and @name='id_gender' and @value='"+gender+"']")[0].click()
driver.find_element_by_xpath("//input[@name='firstname']").send_keys(config['signup']['firstname'].strip())
driver.find_element_by_xpath("//input[@name='lastname']").send_keys(config['signup']['lastname'].strip())
driver.find_element_by_xpath("//input[@name='email']").send_keys(config['signup']['email'].strip())
driver.find_element_by_xpath("//input[@name='password']").send_keys(config['signup']['password'].strip())

checkbox = driver.find_elements_by_xpath("//input[@name='customer_privacy']")[0]
checkbox.click()

checkbox = driver.find_elements_by_xpath("//input[@name='psgdpr']")[0]
checkbox.click()

WebDriverWait(driver, 10);
driver.find_element_by_css_selector(".btn.btn-primary.form-control-submit.float-xs-right").click()


WebDriverWait(driver, 5)
curentUrl= driver.current_url

print ("mainUrl = ["+config['common']['main_url'].strip()+"]")
print ("curentUrl = ["+curentUrl+"]")
#self.assertEqual(expectedurl,config['common']['main_url'], "not the same message")

expectedMessage = config['signup']['firstname'].strip()+" "+config['signup']['lastname'].strip()
contentMessage = driver.find_elements_by_xpath("//span[@class='hidden-sm-down']")[0].text
print ("expectedMessage = ["+expectedMessage+"]")
print ("contentMessage  = ["+contentMessage+"]")
#self.assertTrue(contentMessage in expectedMessage,"Erreur creation du compte")

driver.get_screenshot_as_file("user_signup/02_finalScreen.png")

print ("User sign up test executed succeful ...")

# def load_properties(filepath, sep='=', comment_char='#'):
#     """
#     Read the file passed as parameter as a properties file.
#     """
#     props = {}
#     with open(filepath, "rt") as f:
#         for line in f:
#             l = line.strip()
#             if l and not l.startswith(comment_char):
#                 key_value = l.split(sep)
#                 key = key_value[0].strip()
#                 value = sep.join(key_value[1:]).strip().strip('"') 
#                 props[key] = value 
#     return props