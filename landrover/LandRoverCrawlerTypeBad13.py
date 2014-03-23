SITE_LINKS = {
                "MASSACHUSETTS":[
                                    "http://www.rovercapecod.com/new-land-rover?model=Range+Rover&page=",
                                    "http://www.rovercapecod.com/new-land-rover?model=Range+Rover+Sport&page=",
                                    "http://www.rovercapecod.com/new-land-rover?model=Range+Rover+Evoque&page=",
                                    "http://www.roverhanover.com/new-land-rover?model=Range+Rover&page=",
                                    "http://www.roverhanover.com/new-land-rover?model=Range+Rover+Sport&page=",
                                    "http://www.roverhanover.com/new-land-rover?model=Range+Rover+Evoque&page="
                                 ]
              }

STATES = [
            "MASSACHUSETTS"
          ]


from LandRoverParserTypeBad13 import *

class LandRoverCrawlerTypeBad13:
    def __init__(self,browser,uploader):
        self.browser = browser
        self.parser = LandRoverParserTypeBad13()
        self.uploader = uploader
        
    def MakePagingCompatibleUrl(self,url,nextPageCount):
        return url+str(nextPageCount)
        
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
                allCarLinksForASingleState = []
                if siteLinksForASingleState is not None:
                    for eachSite in siteLinksForASingleState:
                        currentPageCount = 1
                        urlPageOne = self.MakePagingCompatibleUrl(eachSite, currentPageCount)
                        carLinksForASingleLink = []
                        siteDomain = ""
                        page = self.browser.GetPage(urlPageOne)
                        totalResultCount = self.parser.ParseTotalResultCount(page)
                        if totalResultCount is not None and totalResultCount > 0:
                            tempCarLinks = self.parser.ParseCarLinks(siteDomain,page)
                            carLinksForASingleLink.extend(tempCarLinks)
                            while len(tempCarLinks) >= 20:
                                currentPageCount += 1
                                nextPageUrl = self.MakePagingCompatibleUrl(eachSite, currentPageCount)
                                page = self.browser.GetPage(nextPageUrl)
                                tempCarLinks = self.parser.ParseCarLinks(siteDomain,page)
                                carLinksForASingleLink.extend(tempCarLinks)
                        allCarLinksForASingleState.extend(carLinksForASingleLink)
                for eachCarDetailLink in allCarLinksForASingleState:
                    pageSource = self.browser.GetPage(eachCarDetailLink)
                    carDetails = self.parser.ParseCarDetails(eachCarDetailLink,eachState,pageSource)
                    carDetailsList.append(carDetails)
                print "Uploading Started..."
                self.uploader.Upload(carDetailsList)
                print "Uploading Done!"
        except Exception,exp:
            pass
                        
                        
                        
            
            
            
            
            
            
            
    