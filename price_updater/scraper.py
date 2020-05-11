from selenium import webdriver
import re
from ltltlt.models import Price, Item

def getUrl(itemNumber):
    return f'https://www.aliexpress.com/item/{itemNumber}.html'

def getPrice(text):
    pattern = r'\d+\.\d+'
    m = re.search(pattern, text)
    return float(m[0])

def getItemPriceFirefox(itemNumber):
    options = webdriver.firefox.options.Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(getUrl(itemNumber))
    results = driver.find_element_by_class_name('product-price-value').text
    return getPrice(text)

def getItemPriceChrome(itemNumber):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome('chromedriver', options=options)
    driver.get(getUrl(itemNumber))
    results = driver.find_element_by_class_name('product-price-value').text
    return getPrice(results)

def getItemNameChrome(itemNumber):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome('chromedriver', options=options)
    driver.get(getUrl(itemNumber))
    name = driver.find_element_by_class_name('product-title-text').text
    img = driver.find_element_by_class_name('magnifier-image').get_attribute('src')
    driver.quit()
    return name, img

def getItemPrice(itemNumber, driver):
    driver.get(getUrl(itemNumber))
    results = driver.find_element_by_class_name('product-price-value').text
    return getPrice(results)

def updatePrices():
    items = Item.objects.all()

    # setup driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome('chromedriver', options=options)

    for item in items:
        price = Price()
        price.price = getItemPrice(item.item_number, driver)
        price.item_id = item.id 
        price.save()
    
    driver.quit()

