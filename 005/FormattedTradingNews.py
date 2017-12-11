#FormattedTradingNews.py


def storys(data):
	length = len(data)
	for i in range(0, length):
		string = data[i].strip(']')
		print (string)

		
News = open('Todays Crypto news.txt', 'a+')
TradingNews = News.read().split(',')


storys(TradingNews)






	




	
		

	

	

