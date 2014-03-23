SITE_LINKS = {
                "COLORADO":[
                                "http://www.landrovercs.com/web/inventory/All_years/All_makes/Range%20Rover/All_body_types/new/?",
                                "http://www.landroverflatirons.com/web/inventory/All_years/All_makes/Range%20Rover/All_body_types/new/?"
                            ]
              }

STATES = [
                "COLORADO"
              ]


from LandRoverParserTypeBad7 import *

class LandRoverCrawlerTypeBad7:
    def __init__(self,browser,uploader):
        self.browser = browser
        self.parser = LandRoverParserTypeBad7()
        self.uploader = uploader
        
    def FindDomainName(self,pageLink):
        temp = pageLink.replace('http://','')
        indexOfSlash = temp.find('/')
        domainName = ""
        if indexOfSlash != -1:
            domainName = 'http://'+temp[:indexOfSlash]
        return domainName
    
    def MakeNextLinkUrl(self,url,nextPageNumber):
        return url+'start='+str(nextPageNumber)
        
    def StartCrawling(self):
        try:
            for eachState in STATES:
                siteLinksForASingleState = SITE_LINKS.get(eachState)
                allCarDetailsForASingleState = []
                if siteLinksForASingleState is not None:
                    for eachSite in siteLinksForASingleState:
                        start = 0
                        link = self.MakeNextLinkUrl(eachSite, start)
                        page = self.browser.GetPage(link)
                        domainBaseUrl = self.FindDomainName(eachSite)
                        allCarsLinks = []
                        carLinks = self.parser.ParseCarLinks(domainBaseUrl,page)
                        allCarsLinks.extend(carLinks)
                        while len(carLinks) >= 50:
                            start += 50
                            link = self.MakeNextLinkUrl(eachSite, start)
                            page = self.browser.GetPage(link)
                            domainBaseUrl = self.FindDomainName(eachSite)
                            carLinks = self.parser.ParseCarLinks(domainBaseUrl,page)
                            allCarsLinks.extend(carLinks)
                        for eachCarLink in allCarsLinks:
                            pageSource = self.browser.GetPage(eachCarLink)
                            carDetails = self.parser.ParseCarDetails(eachCarLink,eachState,pageSource)
                            allCarDetailsForASingleState.append(carDetails)
                print "Uploading Started..."
                self.uploader.Upload(allCarDetailsForASingleState)
                print "Uploading Done!"
        except Exception,exp:
            pass
                        
                        
                        
            
            
            
            
            
            
            
    