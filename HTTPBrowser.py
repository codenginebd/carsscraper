import urllib2
from random import randint

USER_AGENTS = {
				1:"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
				2:"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
				3:"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
				4:"Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
				5:"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1) Gecko/2008070208 Firefox/3.0.1",
				6:"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14",
				7:"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13",
				8:"Mozilla/4.8 [en] (Windows NT 6.0; U)",
				9:"Mozilla/4.8 [en] (Windows NT 5.1; U)",
				10:"Opera/9.25 (Windows NT 6.0; U; en)",
				11:"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0",
				12:"Opera/7.51 (Windows NT 5.1; U) [en]",
				13:"Opera/7.50 (Windows XP; U)",
				14:"Opera/7.50 (Windows ME; U) [en]",
				15:"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/125.8",
				16:"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/125.2 (KHTML, like Gecko) Safari/85.8",
				17:"Mozilla/4.0 (compatible; MSIE 5.15; Mac_PowerPC)",
				18:"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.7a) Gecko/20050614 Firefox/0.9.0+",
				19:"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-US) AppleWebKit/125.4 (KHTML, like Gecko, Safari) OmniWeb/v563.15",
				20:"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7",
				21:"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5",
				22:"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081216 Ubuntu/8.04 (hardy) Firefox/2.0.0.19",
				23:"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14",
				24:"MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23",
				25:"Opera/9.52 (X11; Linux i686; U; en)",
				26:"Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)",
				27:"Mozilla/3.0 (compatible; NetPositive/2.1.1; BeOS)"
			}

class HTTPBrowser:
	def __init__(self):
		pass
	
	def GetUserAgentRandom(self):
		randomIndex = randint(1,27)
		userAgent = USER_AGENTS.get(randomIndex)
		return userAgent
		
	def GetPage(self,url):
		html = None
		try:
			userAgent = self.GetUserAgentRandom()
			print userAgent
			headers = { 'User-Agent' : userAgent }
			req = urllib2.Request(url, None, headers)
			html = urllib2.urlopen(req).read()
		except Exception,exp:
			pass
		return html