import os, subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
import unittest
import configparser



class TestAcceptanceMethods(unittest.TestCase):

  """ Functional prestashop tests. """
  def setUp(self):
      
      if not os.path.exists('./user_signup'):
          os.makedirs('./user_signup')
      if not os.path.exists('./reports'):
          os.makedirs('./reports')
      else :
          subprocess.run('sudo rm -fr ./reports/*', shell=True)

      self.config = configparser.ConfigParser()
      self.config.read('./config.ini')


      options = Options()
      options.add_argument("--headless")  # Runs Chrome in headless mode.
      options.add_argument('--no-sandbox')  # # Bypass OS security model
      options.add_argument('start-maximized')
      options.add_argument('disable-infobars')
      options.add_argument("--disable-extensions")
      self.driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')
      self.driver.get(self.config['common']['signup_url'].strip())

  def test_usersignup(self):
    driver = self.driver
    config = self.config
    WebDriverWait(driver, 30);
    driver.maximize_window()
    driver.save_screenshot("reports/01_signup_startScreen.png")
    
    gender = config['signup']['gender'].strip()

    driver.find_elements_by_xpath("//input[@type='radio' and @name='id_gender' and @value='" + gender + "']")[0].click()
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

    curentUrl = driver.current_url.strip()
    expectedUrl = config['signup']['expected_url_on_succes'].strip()

    print ("\nexpectedUrl = [" + expectedUrl + "]")
    print ("\ncurentUrl = [" + curentUrl + "]")

    self.assertEqual(curentUrl, expectedUrl, "not the expected url !!")

    subprocess.run('sudo chmod -R 777 ./reports/*', shell=True)
    # driver.maximize_window()
    # driver.save_screenshot("reports/02_signup_finalScreen.png")
    #
    # print ("User sign up test executed succeful ...")

  def tearDown(self):
      self.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="MyReport", add_timestamp=False))
