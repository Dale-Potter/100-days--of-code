#WebScraperTrading

from lxml import html
import requests

page = requests.get('https://www.cryptocoinsnews.com/')
tree = html.fromstring(page.content)

news = tree.xpath('//div[@class="entry-title"]/text()')

todaysNews = open('Todays Crypto news.txt', 'a+')
todaysNews.write(str(news) + '\n')
todaysNews.close()




