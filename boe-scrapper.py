import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# scrappes offers fors the provided day(YYYY/MM/DD)
def scrap_day(day) -> None:
    driver.get('https://www.boe.es/boe/dias/' + day + '/index.php?s=2B')
    time.sleep(2)
    offers = driver.find_elements(by=By.CLASS_NAME, value="dispo")

    for offer in offers:
        if area + ', referente a la convocatoria para proveer' in offer.text:
            offer_text = offer.find_element(by=By.TAG_NAME, value="p").text
            offer_link = offer.find_element(by=By.TAG_NAME, value="a").get_attribute(name="href")
            offer_list.append((offer_text, offer_link))


# parameters
single_day_mode = False # True: scrappes yesterday offers / False: scrappes 'timespan' of days backwards from yesterday
timespan = 5
area = '(Pontevedra)'

# browser configuration
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1200, 900)
driver.implicitly_wait(2) # Increase wait time for slower internet conections

# scrapping
searchDate = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y/%m/%d')
url_template = 'https://www.boe.es/boe/dias/' + searchDate + '/index.php?s=2B'
offer_list = []

if single_day_mode:
    scrap_day(searchDate)
else:
    for i in range(1, timespan + 1):
        searchDate = (datetime.date.today() - datetime.timedelta(days=i)).strftime('%Y/%m/%d')
        weekday = datetime.datetime.strptime(searchDate, '%Y/%m/%d').weekday()
        if weekday != 6:
            scrap_day(searchDate)

for row in offer_list:
    print(row[0] + '\n  -> ' + row[1])
