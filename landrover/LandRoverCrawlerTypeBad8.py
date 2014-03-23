SITE_LINKS = {
                "FLORIDA":[
                        "http://landroverftlauderdale.com/Miami-Fort-Lauderdale/For-Sale/New/Land%20Rover/Range-Rover-Evoque/?FilterNewMakes=0",
                        "http://landroverftlauderdale.com/Miami-Fort-Lauderdale/For-Sale/New/Land%20Rover/Range-Rover-Sport/?FilterNewMakes=0"
                    ],
              "IDAHO":[
                        "http://landroverboise.com/Boise-ID/For-Sale/New/Land%20Rover/Range-Rover-Evoque/?FilterNewMakes=0",
                        "http://landroverboise.com/Boise-ID/For-Sale/New/Land%20Rover/Range-Rover-Sport/?FilterNewMakes=0"
                       ],
              "CALIFORNIA":[
                                "http://landroverencino.com/Encino/For-Sale/New/Land%20Rover/Range-Rover/?FilterNewMakes=0",
                                "http://landroverencino.com/Encino/For-Sale/New/Land%20Rover/Range-Rover-Evoque/?FilterNewMakes=0",
                                "http://landroverencino.com/Encino/For-Sale/New/Land%20Rover/Range-Rover-Sport/?FilterNewMakes=0"
                            ]
              }

STATES = [
            "FLORIDA","IDAHO","CALIFORNIA"
          ]


from LandRoverParserTypeBad8 import *

class LandRoverCrawlerTypeBad8:
    def __init__(self,browser,uploader):
        self.browser = browser
        self.parser = LandRoverParserTypeBad8()
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
                allCarDetailsForASingleState = []
                if siteLinksForASingleState is not None:
                    for eachSite in siteLinksForASingleState:
                        siteDomain = self.FindDomainName(eachSite)
                        page = self.browser.GetPage(eachSite)
                        carDetails = self.parser.ParseCarDetails(siteDomain,eachState,page)
                        carDetailsList.extend(carDetails)
                        pager = self.parser.ParseTotalPageCount(page)
                        if pager is not None and type(pager) is tuple:
                            currentPageCount,totalPageCount = pager
                            while currentPageCount < totalPageCount:
                                nextPageLink = eachSite+"&page="+str(currentPageCount+1)
                                page = self.browser.GetPage(nextPageLink)
                                carDetails = self.parser.ParseCarDetails(siteDomain,eachState,page)
                                allCarDetailsForASingleState.extend(carDetails)
                print "Uploading Started..."
                self.uploader.Upload(allCarDetailsForASingleState)
                print "Uploading Done!"
        except Exception,exp:
            pass
                        
                        
                        
            
            
            
            
            
            
            
    