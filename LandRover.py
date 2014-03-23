from Browser import *
from HTTPBrowser import *
from bs4 import BeautifulSoup
import time
from landrover import *
from Uploader import *

class LandRover:
	def __init__(self):
		browser = HTTPBrowser()
		uploader = Uploader()
		self.landRoverCrawlers = []
		self.landRoverTom = LandRoverCrawlerTypeTom(browser,uploader)
		landRoverTypeBad2 = LandRoverCrawlerTypeBad2(browser,uploader)
		landRoverTypeBad5 = LandRoverCrawlerTypeBad5(browser,uploader)
		landRoverTypeBad7 = LandRoverCrawlerTypeBad7(browser,uploader)
		landRoverTypeBad8 = LandRoverCrawlerTypeBad8(browser,uploader)
		landRoverTypeBad10 = LandRoverCrawlerTypeBad10(browser,uploader)
		landRoverTypeBad13 = LandRoverCrawlerTypeBad13(browser,uploader)
#		self.landRoverCrawlers.append(landRoverTom)
		self.landRoverCrawlers.append(landRoverTypeBad2)
		self.landRoverCrawlers.append(landRoverTypeBad5)
		self.landRoverCrawlers.append(landRoverTypeBad7)
		self.landRoverCrawlers.append(landRoverTypeBad8)
		self.landRoverCrawlers.append(landRoverTypeBad10)
		self.landRoverCrawlers.append(landRoverTypeBad13)
	
	def StartCrawling(self):
		self.landRoverTom.StartCrawling()
		for eachCrawler in self.landRoverCrawlers:
			crawledData = eachCrawler.StartCrawling()