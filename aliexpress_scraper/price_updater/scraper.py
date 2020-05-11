from selenium import webdriver
import re
from ltltlt.models import Price, Item

def _getUrl(itemNumber):
    return f'https://www.aliexpress.com/item/{itemNumber}.html'

def _getPrice(text):
    pattern = r'\d+\.\d+'
    m = re.search(pattern, text)
    return float(m[0])

def getItemPriceFirefox(itemNumber):
    options = webdriver.firefox.options.Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(_getUrl(itemNumber))
    results = driver.find_element_by_class_name('product-price-value').text
    return _getPrice(text)

def getItemNameChrome(itemNumber):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome('chromedriver', options=options)
    driver.get(_getUrl(itemNumber))
    name = driver.find_element_by_class_name('product-title-text').text
    img = driver.find_element_by_class_name('magnifier-image').get_attribute('src')
    price = getItemPrice(itemNumber, driver)
    driver.quit()
    return name, img, price

def getItemPrice(itemNumber, driver):
    driver.get(_getUrl(itemNumber))
    results = driver.find_element_by_class_name('product-price-value').text
    return _getPrice(results)

def updatePrices():
    items = Item.objects.all()

    # setup driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome('chromedriver', options=options)

    for item in items:
        previousPrice = item.price_set.latest('datetime')
        try:
            currentPrice = getItemPrice(item.item_number, driver)
            if currentPrice != previousPrice.price:
                price = Price()
                price.price = currentPrice
                price.item_id = item.id 
                price.save()
        except:
            pass
        
    driver.quit()

