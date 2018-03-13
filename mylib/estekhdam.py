import requests
from bs4 import BeautifulSoup
from urllib.parse import urlsplit

class EstekhdamCrawler:
  def get_results(self, url, keywords, pages):
    """Function that crawl into given number of pages and looks for keywords that you give in the links

      params:
        param1: url: url formatted string
        param2: keywords: list of keywords (list of strings)
        param3: pages: Integer (number of pages to crawl)

      return:
        list of founded links. 
        each items is a dictonary -> {text: value, date: value, link: value}
    """

    matching_links = []

    for i in range(1, pages + 1):
      # print current progress
      print(f'\rProccessing page {i}', end='')

      # for the first page
      if i == 1:
        # crawl the page and get results
        page_items = self.__crawle_page(url)
      else:
        # crawl the page and get results
        page_items = self.__crawle_page(f'{url}/page/{i}')

      # for each link that founded in this page
      # search for given keywords
      for item in page_items:
        if self.__keyword_search(keywords, item['text']):
          matching_links.append(item)

    print(f'\rFounded #{len(matching_links)} matching links')
    return matching_links

  def __keyword_search(self, keywords, text):
    """Simple function that looks given keywords in the text

      params:
          param1: keywords: list of keywords (list of strings)
          param2: text: string
      
      return:
          True: if text contain at least on keyword
          False: if text does not have any of keywords
    """
    for keyword in keywords:
      if keyword.lower() in text.lower():
        return True
    return False


  def __crawle_page(self, url):
    """Function that download a page and extract
    specific links from it.
      params:
            param1: url: url formatted string
      return:
            list of founded links. 
            each items is a dictonary -> {text: value, date: value, link: value}
    """
    # list of items that founded and need to return
    items = []

    # extract domain name from url
    domain = "{0.scheme}://{0.netloc}".format(urlsplit(url))

    # Download url and get html source code
    html_text = requests.get(url).text

    # Load html to b4s
    soup = BeautifulSoup(html_text, 'lxml')

    # find main container that holds search result items
    estekhdam_list = soup.find('div', {'class': 'span7 col-sm-12 col-xs-12 no-margin'})
    estekhdam_soup = BeautifulSoup(str(estekhdam_list), 'lxml')

    # find all of a tags in the main container
    for link in estekhdam_soup.find_all('a', {'class': 'btn btn-link btn-labeled-text btn-large btn-block btn-primary no-margin'}):

      # Extract text and strip it(removing start and end spaces)      
      text = link.contents[-1].strip()

      # Extract date and strip it
      date = link.contents[1].text.strip()

      # Extract href and concat it with domain (for pretty link)      
      link = domain + link['href']

      json = {'text': text, 'date': date, 'link': link}
      items.append(json)

    return items
