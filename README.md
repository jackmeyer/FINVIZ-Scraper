# FINVIZ-Scraper
A simple Selenium/BeautifulSoup web scraping tool that returns all commodity futures on FINVIZ into a dictionary.

This Python script utilizes a Selenium PhantomJS headless browser to load all JavaScript-generated content on the FINVIZ Commodity Futures page and uses BeautifulSoup to parse the HTML and search for specific tags.

## Dependencies
 - Selenium (installed via `npm install selenium`)
 - BeautifulSoup (installed via `npm install bs4 `)
 - PhantomJS WebDriver ([download](http://phantomjs.org/download.html) .exe and save in same folder as FINVIZ-Scraper)
