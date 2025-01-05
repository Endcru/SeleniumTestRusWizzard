import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re, time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def test_1(self):
        driver = self.driver
        driver.get("http://ruswizard.ddns.net:8091/")
        self.assertIn("SBTS", driver.title)
        elem = driver.find_element(By.ID, "sessionId")
        session_value = elem.get_attribute("value")
        elem_open = driver.find_element(By.ID, "login-btn")
        elem_open.send_keys(Keys.RETURN)
        elem_arrowLeft = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "arrowLeft")))
        elem_arrowLeft.click()
        time.sleep(3)
        elem_text = driver.find_element(By.ID, "text").text
        saved_elem_text = elem_text
        elem_exit = driver.find_element(By.ID, "logout-btn")
        elem_exit.click()
        time.sleep(3)
        self.assertEqual(session_value, driver.find_element(By.ID, "sessionId").get_attribute("value"))
        for i in range(0, 100):
            elem_open = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login-btn")))
            elem_open.click()
            time.sleep(2)
            elem_text = driver.find_element(By.ID, "text").text
            self.assertEqual(elem_text, saved_elem_text)
            elem_exit.click()
    
    def test_2(self):
        driver = self.driver
        driver.get("http://ruswizard.ddns.net:8091/")
        self.assertIn("SBTS", driver.title)
        elem = driver.find_element(By.ID, "sessionId")
        session_value = elem.get_attribute("value")
        print(session_value)
        elem_open = driver.find_element(By.ID, "login-btn")
        elem_open.send_keys(Keys.RETURN)
        elem_arrowLeft = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "arrowLeft")))
        elem_arrowRight = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "arrowRight")))
        for i in range(0, 30):
            elem_arrowLeft.click()
        time.sleep(3)
        elem_text = driver.find_element(By.ID, "place").text
        print(elem_text)
        self.assertNotEqual(elem_text, 'Море [-30]')

    def test_3(self):
        driver = self.driver
        driver.get("http://ruswizard.ddns.net:8091/")
        self.assertIn("SBTS", driver.title)
        elem = driver.find_element(By.ID, "sessionId")
        session_value = elem.get_attribute("value")
        print(session_value)
        elem_open = driver.find_element(By.ID, "login-btn")
        elem_open.send_keys(Keys.RETURN)
        elem_exit = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "logout-btn")))
        elem_exit.click()
        elem_open = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login-btn")))
        elem_open.click()
        elem_arrowLeft = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "arrowLeft")))
        elem_arrowRight = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "arrowRight")))
        time.sleep(3)
        elem_arrowLeft.click()
        time.sleep(3)
        elem_text = driver.find_element(By.ID, "text").text
        saved_elem_text = elem_text
        elem_exit = driver.find_element(By.ID, "logout-btn")
        elem_exit.click()
        time.sleep(3)
        self.assertEqual(session_value, driver.find_element(By.ID, "sessionId").get_attribute("value"))
        for i in range(0, 100):
            elem_open = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "login-btn")))
            elem_open.click()
            time.sleep(3)
            elem_text = driver.find_element(By.ID, "text").text
            print("New text =", elem_text)
            self.assertEqual(elem_text, saved_elem_text)
            elem_exit = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "logout-btn")))
            elem_exit.click()
    
    def test_4(self):
        driver = self.driver
        driver.get("http://ruswizard.ddns.net:8091/")
        self.assertIn("SBTS", driver.title)
        elem = driver.find_element(By.ID, "sessionId")
        session_value = elem.get_attribute("value")
        print(session_value)
        elem_open = driver.find_element(By.ID, "login-btn")
        elem_open.send_keys(Keys.RETURN)
        elem_arrowLeft = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "arrowLeft")))
        elem_arrowRight = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "arrowRight")))
        for i in range(0, 19):
            elem_arrowLeft.click()
        time.sleep(3)
        elem_text = driver.find_element(By.ID, "place").text
        self.assertNotEqual(elem_text[-5:], '[-19]')
        
    def test_5(self):
        driver = self.driver
        driver.get("http://ruswizard.ddns.net:8091/")
        self.assertIn("SBTS", driver.title)
        elem = driver.find_element(By.ID, "sessionId")
        session_value = elem.get_attribute("value")
        print(session_value)
        elem_open = driver.find_element(By.ID, "login-btn")
        elem_open.send_keys(Keys.RETURN)
        elem_act_0 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "act-0-0")))
        elem_act_0.click()
        time.sleep(5)
        elem_item1007buy = driver.find_element(By.ID, "item1007buy")
        driver.execute_script("arguments[0].scrollIntoView(true);", elem_item1007buy)
        elem_item1007buy.click()
        time.sleep(3)
        elem_text = driver.find_element(By.ID, "moneyDock").text
        print('!!!!', elem_text)
        saved_elem_text = elem_text
        elem_itemsell1007cnt = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "itemsell1007cnt")))
        elem_itemsell1007cnt .send_keys('100')
        elem_item1007sell = driver.find_element(By.ID, "item1007sell")
        elem_item1007sell.click()
        time.sleep(3)
        elem_text = driver.find_element(By.ID, "moneyDock").text
        self.assertEqual(saved_elem_text, elem_text)
        
    
    def test_6(self):
        self.driver.close()
    

if __name__ == "__main__":
    unittest.main()