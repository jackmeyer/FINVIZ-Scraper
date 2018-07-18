from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

#launch URL
url = "https://finviz.com/futures.ashx"

#create a new Chrome session

driver = webdriver.PhantomJS()


driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

tickers = []
prices = []
tickers1 = []
prices1 = []

tickers = soup.find_all('div', class_ = "tile_label")
prices = soup.find_all('div', class_ = "tile_last-price")

for x in prices:
  prices1.append(x.text)

for x in tickers:
  tickers1.append(x.text)

together = dict(zip(tickers1, prices1))

print(together)
