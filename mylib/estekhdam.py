import requests
from bs4 import BeautifulSoup
from urllib.parse import urlsplit


class EstekhdamCrawler:
    def get_results(self, url, keywords):
        """Function that crawl into given number of pages and looks for keywords that you give in the links

          params:
            param1: url: url formatted string
            param2: keywords: list of keywords (list of strings)
            param3: pages: Integer (number of pages to crawl)

          return:
            list of founded links.
            each items is a dictonary -> {text: value, date: value, link: value}
        """
        today = None
        matching_links = []
        page = 1
        while True:
            # print current progress
            print('\rProccessing page {}'.format(page), end='')

            # for the first page
            if page == 1:
                # crawl the page and get results
                page_items, limit_reached = self.__crawl_page(url)
            else:
                # crawl the page and get results
                page_items, limit_reached = self.__crawl_page('{0}/page/{1}'.format(url, page), today)

            page += 1

            # for each link that founded in this page
            # search for given keywords
            for item in page_items:
                if self.__keyword_search(keywords, item['text']):
                    matching_links.append(item)

            if limit_reached:
                print('\nToday links are finished.')
                break

        print('\rFounded #{} matching links'.format(len(matching_links)))
        return matching_links

    @staticmethod
    def __keyword_search(keywords, text):
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

    @staticmethod
    def __crawl_page(url, today=None):
        """Function that download a page and extract
        specific links from it.
          params:
                param1: url: url formatted string
                param2: today: string of today date
          return:
                (list of founded links, Limit Reached Status)
                each items is a dictonary -> {text: value, date: value, link: value}
                True -> today items run out
                False -> keep going
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
        for link in estekhdam_soup.find_all('a', {
            'class': 'btn btn-link btn-labeled-text btn-large btn-block btn-primary no-margin'}):
            # Extract text and strip it(removing start and end spaces)
            text = link.contents[-1].strip()

            # Extract date and strip it
            date = link.contents[1].text.strip()

            # Extract href and concat it with domain (for pretty link)
            link = domain + link['href']

            json = {'text': text, 'date': date, 'link': link}

            # if today is none we set it to date of first item we see
            if today is None:
                today = json['date']

            if json['date'] == today:
                items.append(json)
            else:
                return items, True

        return items, False
