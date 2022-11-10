from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get('http:/localhost:8080')

driver.find_element(By.ID, "add-movie").click()

driver.find_element(By.NAME, "title").send_keys("Shrek")
driver.find_element(By.NAME, "year").send_keys("2001")
driver.find_element(By.NAME, "director").send_keys("Andrew Adamson")
driver.find_element(By.NAME, "rating").send_keys("5")
driver.find_element(By.NAME, "review").send_keys("Shrek es un ogro verde, gruñón y altamente territorial que ama la soledad.")

driver.find_element(By.CLASS_NAME, "btn-primary").send_keys(Keys.ENTER)

time.sleep(3)

driver.find_element(By.ID, "add-movie").click()

driver.find_element(By.NAME, "title").send_keys("Braveheart")
driver.find_element(By.NAME, "year").send_keys("1995")
driver.find_element(By.NAME, "director").send_keys("Miel Gibson")
driver.find_element(By.NAME, "rating").send_keys("5")
driver.find_element(By.NAME, "review").send_keys("Cinta épica, basada en la vida de William Wallace, un héroe nacional escocés que participó en la Primera Guerra de Independencia de Escocia.")

driver.find_element(By.CLASS_NAME, "btn-primary").send_keys(Keys.ENTER)

time.sleep(3)

driver.find_element(by=By.XPATH, value="//a[@href='/edit/1']").click()
driver.find_element(By.NAME, "review").clear()
driver.find_element(By.NAME, "review").send_keys("Gran adaptación de una novela clásica de ciencia ficción.")
driver.find_element(By.CLASS_NAME, "btn-primary").send_keys(Keys.ENTER)

time.sleep(3)

driver.find_element(by=By.XPATH, value="//a[@href='/edit/2']").click()
driver.find_element(By.NAME, "review").clear()
driver.find_element(By.NAME, "review").send_keys("Emocionante película biográfica estilizada del Rey.")
driver.find_element(By.CLASS_NAME, "btn-primary").send_keys(Keys.ENTER)

driver.quit()


