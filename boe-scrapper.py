from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# parameters
area = 'Pontevedra'
date = '2023/08/22'
url_template = 'https://www.boe.es/boe/dias/' + date + '/index.php?s=2B'

# browser configuration
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1200, 900)
driver.implicitly_wait(5)

# scrapping
try:
    driver.get(url_template)
    time.sleep(2)
    offers = driver.find_elements(by=By.CLASS_NAME, value="dispo")
except Exception:
    print("peto")

offerList = []

for offer in offers:
    if '(Pontevedra), referente a la convocatoria para proveer' in offer.text:
        offerText = offer.find_element(by=By.TAG_NAME, value="p").text
        offerLink = offer.find_element(by=By.TAG_NAME, value="a").get_attribute(name="href")
        offerList.append((offerText, offerLink))

print(offerList)