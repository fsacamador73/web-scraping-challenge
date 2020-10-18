from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dic = {}

    from bs4 import BeautifulSoup as bs
    import os
    import requests
    from splinter import Browser
    from bs4 import BeautifulSoup
    from splinter.exceptions import ElementDoesNotExist
    import cssutils
    import pandas as pd
    import time

    # https://splinter.readthedocs.io/en/latest/drivers/chrome.html
    #!which chromedriver

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    mars_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(mars_url)

    time.sleep(3)

    mars_dict = {}
    mars_title = []
    mars_news = []
    
    # Iterate through all pages
    for x in range(1):
        # HTML object
        html = browser.html
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        # Retrieve all elements that contain information
        results = soup.find_all('div', class_='list_text')

        # Iterate through each result
        for result in results:
            # Use Beautiful Soup's find() method to navigate and retrieve attributes
            news_title = result.find('div', class_='content_title').text
            news_p = result.find('div', class_='article_teaser_body').text

            print('-----------')
            print("News Title: ", news_title, "\n")
            print("Abstract: ", news_p, "\n")

            mars_dict.update({"news_title" : news_title, "news_p" : news_p})
            mars_title.append(news_title)
            mars_news.append(news_p)



    mars_dict
    mars_dic['mars_dict'] = mars_dict

    mars_title = mars_title[0]
    mars_title
    mars_dic['mars_title'] = mars_title

    mars_news = mars_news[0]
    mars_news
    mars_dic['mars_news'] = mars_news


    img_url = 'https://www.jpl.nasa.gov'
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)

    # Iterate through all pages
    #for x in range(1):
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain information
    results = soup.find_all('article', class_='carousel_item')
    print(results)

    div_style = soup.find('article', class_='carousel_item')['style']
    style = cssutils.parseStyle(div_style)
    url = style['background-image']
    url = url.replace('url(', '').replace(')', '')
    url

    featured_image_url = (img_url + url)
    featured_image_url

    print('-----------')
    print("Featured Image URL: ", featured_image_url, "\n")

    mars_dic['feat_img_url'] = featured_image_url

    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)

    time.sleep(3)

    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain information
    results = soup.find_all('span', class_='css-901oao')[43].text
    results

    print('-----------')
    print("Mars Weather: ", results, "\n")

    mars_dic['results'] = results

    df_url = 'https://space-facts.com/mars/'

    mars_data_df = pd.read_html(df_url)
    mars_data_df

    type(mars_data_df)

    df = mars_data_df[0]
    df.columns = ['Characteristic', 'Value']
    df

    df.set_index('Characteristic', inplace=True)
    df

    html_table = df.to_html()
    html_table

    html_table.replace('\n', '')
    html_table

    df.to_html('mars_facts_table.html')

    #!open mars_facts_table.html

    mars_dic['html_table'] = html_table

    base_url = 'https://astrogeology.usgs.gov'

    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)

    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all elements that contain information
    results = soup.find_all('a', class_='itemLink')

    url_list = []

    for result in results:
        href = result['href']
        h1 = (base_url + href)
        url_list.append(h1)

    url_list

    h1 = url_list[0]
    h1

    h2 = url_list[2]
    h2

    h3 = url_list[4]
    h3

    h4 = url_list[6]
    h4

    h1 = h1
    browser.visit(h1)

    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all elements that contain information
    results = soup.find('img', class_='wide-image')
    results

    h1_img = results['src']
    h1_img = (base_url + h1_img)
    h1_img
    mars_dic['h1_img'] = h1_img

    h1_title = soup.find('h2', class_='title').text
    h1_title
    mars_dic['h1_title'] = h1_title

    h1_dic = [{h1_img, h1_title}]
    h1_dic

    h2 = h2
    browser.visit(h2)

    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all elements that contain information
    results = soup.find('img', class_='wide-image')
    results

    h2_img = results['src']
    h2_img = (base_url + h2_img)
    h2_img
    mars_dic['h2_img'] = h2_img

    h2_title = soup.find('h2', class_='title').text
    h2_title
    mars_dic['h2_title'] = h2_title

    h2_dic = [{h2_img, h2_title}]
    h2_dic

    h3 = h3
    browser.visit(h3)

    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all elements that contain information
    results = soup.find('img', class_='wide-image')
    results

    h3_img = results['src']
    h3_img = (base_url + h3_img)
    h3_img
    mars_dic['h3_img'] = h3_img

    h3_title = soup.find('h2', class_='title').text
    h3_title
    mars_dic['h3_title'] = h3_title

    h3_dic = [{h3_img, h3_title}]
    h3_dic

    h4 = h4
    browser.visit(h4)

    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all elements that contain information
    results = soup.find('img', class_='wide-image')
    results

    h4_img = results['src']
    h4_img = (base_url + h4_img)
    h4_img
    mars_dic['h4_img'] = h4_img

    h4_title = soup.find('h2', class_='title').text
    h4_title
    mars_dic['h4_title'] = h4_title

    h4_dic = [{h4_img, h4_title}]
    h4_dic

    hemisphere_image_urls = [{'Title':h1_title, 'img_url':h1_img}, {'Title':h2_title, 'img_url':h2_img}, {'Title':h3_title, 'img_url':h3_img}, {'Title':h4_title, 'img_url':h4_img}]
    hemisphere_image_urls

    hemisphere_image_urls = [{'Title':'Cerberus Hemisphere', 'img_url':'https://astrogeology.usgs.gov/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'}, {'Title':'Schiaparelli Hemisphere', 'img_url':'https://astrogeology.usgs.gov/cache/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'}, {'Title':'Syrtis Major Hemisphere', 'img_url':'https://astrogeology.usgs.gov/cache/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'}, {'Title':'Valles Marineris Hemisphere', 'img_url':'https://astrogeology.usgs.gov/cache/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'}]
    hemisphere_image_urls

    return mars_dic