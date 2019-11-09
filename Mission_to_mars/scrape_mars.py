# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup

# Function to set up the browser path
def init_browser():
    # Configure browser for scraping
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

# Function to perform the actual scraping
def scrape():
    browser = init_browser()
    response = {}
    # Define URL variables
    nasaURL = "https://mars.nasa.gov/news/"
    jplURL = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    twitterURL = 'https://twitter.com/marswxreport?lang=en'
    astrogeologyURL = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    marsFactsURL = 'https://space-facts.com/mars/'


    ## Scrape NASA Mars news
    # Launch the browser
    browser.visit(nasaURL)
        # Pull in browser content to form the soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find('div', class_='list_text')
    titleLevel1 = results.find('div', class_='content_title')
    news_title = titleLevel1.find('a').text
    news_p = results.find('div', class_='article_teaser_body').text
    response.update( {'News Title' : news_title} )
    response.update( {'News Paragraph' : news_p} )
    print("Completed")


    return response
