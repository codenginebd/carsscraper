SITE_LINKS = {
                "CALIFORNIA":[
                                "http://www.hornburgla.com/vehicle/search/new/land%20rover/range%20rover/?",
                                "http://www.hornburgla.com/vehicle/search/new/land%20rover/range%20rover%20evoque/?",
                                "http://www.hornburgla.com/vehicle/search/new/land%20rover/range%20rover%20sport/?",
                                "http://www.hornburgsantamonica.com/vehicle/search/new/Land%20Rover/range%20rover/?",
                                "http://www.hornburgsantamonica.com/vehicle/search/new/Land%20Rover/range%20rover%20evoque/?",
                                "http://www.hornburgsantamonica.com/vehicle/search/new/Land%20Rover/range%20rover%20sport/?"
                              ]
              }

STATES = [
            "CALIFORNIA"
          ]


from LandRoverParserTypeBad5 import *

class LandRoverCrawlerTypeBad5:
    def __init__(self,browser,uploader):
        self.browser = browser
        self.parser = LandRoverParserTypeBad5()
        self.uploader = uploader
        
    def MakePagingCompatibleUrl(self,url,nextPageCount):
        return url+"page="+str(nextPageCount)
        
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
                        siteDomain = self.FindDomainName(eachSite)
                        page = self.browser.GetPage(urlPageOne)
                        totalResultCount = self.parser.ParseTotalResultCount(page)
                        if totalResultCount is not None and totalResultCount > 0:
                            tempCarLinks = self.parser.ParseCarLinks(siteDomain,page)
                            carLinksForASingleLink.extend(tempCarLinks)
                            while len(tempCarLinks) >= 25:
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
                        
                        
                        
            
            
            
            
            
            
            
    