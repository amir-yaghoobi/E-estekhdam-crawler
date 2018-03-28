import config
import json
from mylib.estekhdam import EstekhdamCrawler
from validators import url as urlValidator
from mylib.bot import NotificationBot


def check_configs():
    """function that validate values in config.py
    """
    validation_flag = True

    # check url pattern for site url
    if not urlValidator(config.SITE_URL):
        validation_flag = False
        print('ERROR: SITE_URL in config.py file is invalid. please replace it with a valid url')

    # check KEYWORD is a list
    if not isinstance(config.KEYWORDS, list):
        validation_flag = False
        print('ERROR: KEYWORDS in config.py file is invalid. we require a list.')

        # check KEYWORDS are not a empty list
    if len(config.KEYWORDS) < 1:
        validation_flag = False
        print('ERROR: KEYWORDS in config.py file. Please put one or more than one keywords to search.')

    # return validation result
    return validation_flag


def main():
    print('*********************************')
    print('|      E-estekhdam Crawler      |')
    print('*********************************')

    # check if config file is valid or not
    if not check_configs():
        print('---------------------------------')
        print('Please fix the above problems and then run the program.')
        return

    print('Starting with these settings')
    print(f'\tUrl: {config.SITE_URL}')
    print(f'\tKeywords: {config.KEYWORDS}')
    crawler = EstekhdamCrawler()
    result = crawler.get_results(config.SITE_URL, config.KEYWORDS)
    bot = NotificationBot(config.BOT_TOKEN, config.CHANNEL_ID)

    for r in result:
        msg = '{0}\n[مشاهده آگهی]({2})\n📅  {1}'.format(r['text'], r['date'], r['link'])
        bot.send_message(msg)
    # write results to file
    with open('result.json', 'w+', encoding='utf8') as mfile:
        json.dump(result, mfile, ensure_ascii=False,
                  indent=4, separators=(',', ': '))

    print('result is saved into result.json file.')
    print('\n|  Developed by: Amirhossein Yaghoobi.  |')


if __name__ == '__main__':
    main()
