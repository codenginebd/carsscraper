SITE_LINKS = {
                "ALABAMA":[
                            "http://www.centurylandroverhuntsville.com/inventory-huntsville-new_cars-land_rover-range_rover.html",
                            "http://www.centurylandroverhuntsville.com/inventory-huntsville-new_cars-land_rover-range_rover_evoque.html",
                            "http://www.centurylandroverhuntsville.com/inventory-huntsville-new_cars-land_rover-range_rover_sport.html"
                           ]
              }

STATES = [
            "ALABAMA"
          ]


from LandRoverParserTypeBad2 import *

class LandRoverCrawlerTypeBad2:
    def __init__(self,browser,uploader):
        self.browser = browser
        self.parser = LandRoverParserTypeBad2()
        self.uploader = uploader
        
    def FindDomainName(self,pageLink):
        temp = pageLink.replace('http://','')
        indexOfSlash = temp.find('/')
        domainName = ""
        if indexOfSlash != -1:
            domainName = 'http://'+temp[:indexOfSlash]
        return domainName
        
    def StartCrawling(self):
        try:
            for eachState in STATES:
                siteLinksForASingleState = SITE_LINKS.get(eachState)
                carDetailsList = []
                if siteLinksForASingleState is not None:
                    for eachSite in siteLinksForASingleState:
                        page = self.browser.GetPage(eachSite)
                        totalResult = self.parser.ParsePageCount(page)
                        totalPaging = totalResult/100 + 1
                        carLinks = []
                        carLinks = self.parser.ParseCarLinks("",page)
                        totalPagingLinks = []
                        pagingLinks = self.parser.ParsePagingLinks(page)
                        totalPagingLinks.extend(pagingLinks)
                        if len(pagingLinks) > 0 and int(pagingLinks[len(pagingLinks) - 1].get("label")) < totalPaging:
                            lastPagingLink = pagingLinks[len(pagingLinks) - 1].get("link")
                            page = self.browser.GetPage(lastPagingLink)
                            pagingLinks = self.parser.ParsePagingLinks(page)
                            totalPagingLinks.extend(pagingLinks)
                        ###Remove duplicates
                        totalPagingLinks = list(set(totalPagingLinks))
                        for key,value in totalPagingLinks:
                            page = self.browser.GetPage(value)
                            tempCarLinks = self.parser.ParseCarLinks("",page)
                            carLinks.extend(tempCarLinks)
                        carLinks = list(set(carLinks))
                        carDetailsListTemp = []
                        for eachCarLink in carLinks:
                            pageSource = self.browser.GetPage(eachCarLink)
                            carDetails = self.parser.ParseCarDetails(eachCarLink,eachState,pageSource)
                            carDetailsListTemp.append(carDetails)
                        carDetailsListTemp = list(set(carDetailsListTemp))
                        self.uploader.Upload(carDetailsListTemp)
#                        carDetailsList = list(set(carDetailsList))
        except Exception,exp:
            pass
                        
                        
                        
            
            
            
            
            
            
            
    