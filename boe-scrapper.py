from selenium import webdriver
from selenium.webdriver.common.by import By

# parameters
area = 'Pontevedra'
date = '2023/08/22'
url_template = 'https://www.boe.es/boe/dias/' + date + '/index.php?s=2B'

# browser configuration
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1200, 900)
driver.implicitly_wait(3)

# scrapping
driver.get(url_template)
text_box = driver.find_element(by=By.NAME, value="el")
