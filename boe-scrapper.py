import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
from datetime import timedelta
import time


def scrap_day(day) -> None:
    driver.get('https://www.boe.es/boe/dias/' + day + '/index.php?s=2B')
    time.sleep(2)
    offers = driver.find_elements(by=By.CLASS_NAME, value="dispo")

    for offer in offers:
        if area + ', referente a la convocatoria para proveer' in offer.text:
            offer_text = offer.find_element(by=By.TAG_NAME, value="p").text
            offer_link = offer.find_element(by=By.TAG_NAME, value="a").get_attribute(name="href")
            offerList.append((offer_text, offer_link))


# parameters
singleDayMode = False
timespan = 20
area = '(Pontevedra)'

# browser configuration
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1200, 900)
driver.implicitly_wait(2)

# scrapping
searchDate = (date.today() - datetime.timedelta(days=1)).strftime('%Y/%m/%d')
url_template = 'https://www.boe.es/boe/dias/' + searchDate + '/index.php?s=2B'

offerList = []

if singleDayMode:
    scrap_day(searchDate)
else:
    for i in range(1, timespan + 1):
        searchDate = (date.today() - datetime.timedelta(days=i)).strftime('%Y/%m/%d')
        scrap_day(searchDate)

for row in offerList:
    print(row[0] + '  -> ' + row[1])
