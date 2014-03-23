from HTTPBrowser import *
from Porsche import *
from MarcedesBenz import *
import json
from landrover import *

#browser = HTTPBrowser()
#for i in range(20):
#	print i + 1
#	browser.GetPage("http://jack-ingram.porschedealer.com/new/Porsche/Cayenne/search.php")

#f = open("porsche_details.html","r")
#contents = f.read()
#f.close()
#porscheScraper = PorscheScraper()
##print porscheScraper.ScrapeAllCarsLinks("http://jack-ingram.porschedealer.com",contents)
#print porscheScraper.ScrapeCarDetails(contents)

#porsche = Porsche()
#print porsche.StartCrawling()

#f = open("Marcedes.html","r")
#contents = f.read()
#f.close()
#marcedesParser = MarcedesParser()
#print marcedesParser.ParseTotalPageCount(contents)
#f = open("Marcedes_details.html","r")
#contents = f.read()
#f.close()
#marcedesParser = MarcedesParser()
#r = marcedesParser.ParseCarDetails("http://www.crown.mercedesdealer.com/new/2013/mercedes/s550/2013-mercedes-s550-silver-hoover-for-sale-wddng7db3da535206","Amabama",contents)
#print json.dumps(r,indent=4)

#marcedesBenz = MarcedesBenz()
#print marcedesBenz.StartCrawling()

#f = open("LandRoverDetails.html","r")
#contents = f.read()
#f.close()
#landRover = LandRoverParserTypeTom()
#details = landRover.ParseCarDetails("http://www.tomwilliamslandrover.com/new/Land+Rover/2014-Land+Rover-Range+Rover-Birmingham-8c6522610a0a00de00be6d81901684e1.htm",contents)
#print json.dumps(details,indent=4)


#landRover = LandRoverCrawlerTypeTom(HTTPBrowser())
#landRover.StartCrawling()

#f = open("LandRoverDetails.html","r")
#contents = f.read()
#f.close()
#landRover = LandRoverParserTypeBad13()
#d= landRover.ParseCarDetails("","",contents)
##print len(d)
##d = landRover.ParseCarDetails("http://www.hornburgla.com/vehicle/specs/land%20rover/range%20rover/2014/vin/SALGS2VF4EA128544","CALIFORNIA",contents)
#print json.dumps(d,indent=4)

# landRover = LandRoverCrawlerTypeBad2(HTTPBrowser())
# r = landRover.StartCrawling()
# print r
# print len(r)

#porsche = LandRoverCrawlerTypeBad2(HTTPBrowser())
#porsche.StartCrawling()

data = {"data":[{"title":"Demo Title","price":"$30000","link":"Sample Link","state":"State","year":"year","make":"Make","exterior":"Exterior","interior":"Interior","vin":"VIN","phone":"Phone","location":"Location","mileage":"Mileage"}]}
req = urllib2.Request("http://codenginebd.appspot.com/service/upload/", data=json.dumps(data),headers={"Content-Type": "application/json"})
urllib2.urlopen(req).read()

