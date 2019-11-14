# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup


# Function to perform the actual scraping
def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    response = {}
    # Define URL variables
    nasaURL = "https://mars.nasa.gov/news/"
    jplURL = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    twitterURL = 'https://twitter.com/marswxreport?lang=en'
    astrogeologyURL = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    marsFactsURL = 'https://space-facts.com/mars/'

    print("Beginning scrape")

    try:
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
        response.update( {'news_title' : news_title} )
        response.update( {'news_paragraph' : news_p} )
    except:
        print("News title and paragraph failed")

    try:
        ## Scrape JPL Mars Space Images for the Featured Image
        # Launch the browser
        browser.visit(jplURL)

        # Pull in browser content to form the soup
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        # Narrow the search scope to the container of the featured image
        results = soup.find('article', class_='carousel_item')

        # Extract the URL of the hero image
        imageURL = results.find('a')["data-fancybox-href"]

        # Create the full image URL
        baseURL = 'https://www.jpl.nasa.gov'
        featured_image_URL = baseURL + imageURL

        # Append results to dictionary
        response.update( {'featured_image_URL' : featured_image_URL} )

    except:
        print("Feature image failed")

    try:
        ## Scrape the Mars Weather Twitter Account
        # Launch the browser
        browser.visit(twitterURL)

        # Pull in browser content to form the soup
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        # Narrow the search scope to the container of the first tweet
        results = soup.find('div', class_='js-tweet-text-container')

        # Pull out just the tweet's content
        mars_weather = results.find('p').text

        response.update( {'mars_weather' : mars_weather} )

    except:
        print("Twitter weather scraping failed")


#    try:
#        ## Scrape the Mars Facts site
#        # Launch the browser
#        browser.visit(marsFactsURL)
#
#        # Pull in browser content to form the soup
#        html = browser.html
#        soup = BeautifulSoup(html, 'html.parser')
#        factTable = soup.find('table')
#        response.update( {'fact_table' : factTable} )
#
#    except:
#        print("Fact table failed")


    try:
        ## Scrape the USGS Astrogeology site
        # Declare variables
        hemisphere_image_urls = []

        # Cerberus Hemisphere
        # Open the main page
        browser.visit(astrogeologyURL)

        # Open the link
        browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')

        # Pull in browser content to form the soup
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        # Pull the original image title
        title = soup.find('h2', class_='title').text

        # Pull the original image URL
        for i in soup.find_all('a'):
            target = 'Original'
            if i.text == target:
                img_url = i['href']


        # Add results to response dict
        response.update( {'hemisphere_title_cerberus' : title} )
        response.update( {'hemisphere_img_cerberus' : img_url} )


        # Schiaparelli Hemisphere
        # Open the main page
        browser.visit(astrogeologyURL)

        # Open the link
        browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')

        # Pull in browser content to form the soup
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        # Pull the original image title
        title = soup.find('h2', class_='title').text

        # Pull the original image URL
        for i in soup.find_all('a'):
            target = 'Original'
            if i.text == target:
                img_url = i['href']

        # Add results to response dict
        response.update( {'hemisphere_title_schiaparelli' : title} )
        response.update( {'hemisphere_img_schiaparelli' : img_url} )

        # Syrtis Major Hemisphere
        # Open the main page
        browser.visit(astrogeologyURL)

        # Open the link
        browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')

        # Pull in browser content to form the soup
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        # Pull the original image title
        title = soup.find('h2', class_='title').text

        # Pull the original image URL
        for i in soup.find_all('a'):
            target = 'Original'
            if i.text == target:
                img_url = i['href']

        # Add results to response dict
        response.update( {'hemisphere_title_syrtis' : title} )
        response.update( {'hemisphere_img_syrtis' : img_url} )

        # Valles Marineris Hemisphere
        # Open the main page
        browser.visit(astrogeologyURL)

        # Open the link
        browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')

        # Pull in browser content to form the soup
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        # Pull the original image title
        title = soup.find('h2', class_='title').text

        # Pull the original image URL
        for i in soup.find_all('a'):
            target = 'Original'
            if i.text == target:
                img_url = i['href']

        # Add results to response dict
        response.update( {'hemisphere_title_marineris' : title} )
        response.update( {'hemisphere_img_marineris' : img_url} )


    except:
        print("Hemisphere images failed")

    # Close the browser
    browser.quit()

    # Print response to console for debugging
    print(response)
    print("Scrape complete")

    return response
