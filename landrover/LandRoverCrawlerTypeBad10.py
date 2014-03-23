SITE_LINKS = {
                "MASSACHUSETTS":[
                        "http://jaguarlandrovernorwood.com/inventory/view/Model/Range%20Rover/New/Records50/",
                        "http://jaguarlandrovernorwood.com/inventory/view/Model/Range%20Rover%20Evoque/New/Records50/",
                        "http://jaguarlandrovernorwood.com/inventory/view/Model/Range%20Rover%20Sport/New/records50/"
                    ],
              "CALIFORNIA":[
                                "http://www.landroversj.com/inventory/view/Model/Range%20Rover/New/Records50/",
                                "http://www.landroversj.com/inventory/view/Model/Range%20Rover%20Evoque/New/Records50/",
                                "http://www.landroversj.com/inventory/view/Model/Range%20Rover%20Sport/New/Records50/"
                            ],
              "FLORIDA":[
                            "http://www.landroverpalmbeach.com/inventory/view/Model/Range%20Rover%20Evoque/New/Records50/",
                            "http://www.landroverpalmbeach.com/inventory/view/Model/Range%20Rover%20Sport/New/Records50/",
                            "http://www.landroverpalmbeach.com/inventory/view/Model/Range%20Rover/New/Records50/"
                         ],
              "GEORGIA":[
                            "http://www.landrovergwinnett.com/inventory/view/Model/Range%20Rover%20Evoque/New/Records50/",
                            "http://www.landrovergwinnett.com/inventory/view/Model/Range%20Rover%20Sport/New/Records50/",
                            "http://www.landrovergwinnett.com/inventory/view/Model/Range%20Rover/New/Records50/",
                            "http://www.landrovernorthpoint.com/inventory/view/Model/Range%20Rover%20Evoque/New/Records50/",
                            "http://www.landrovernorthpoint.com/inventory/view/Model/Range%20Rover%20Sport/New/Records50/",
                            "http://www.landrovernorthpoint.com/inventory/view/Model/Range%20Rover/New/Records50/"
                         ]
              }

STATES = [
            "MASSACHUSETTS","CALIFORNIA","FLORIDA","GEORGIA"
          ]

DIR_URL = "/SortBy0/"


from LandRoverParserTypeBad10 import *

class LandRoverCrawlerTypeBad10:
    def __init__(self,browser,uploader):
        self.browser = browser
        self.parser = LandRoverParserTypeBad10()
        self.uploader = uploader
        
    def MakePagingCompatibleUrl(self,url,nextPageCount):
        return url+"Page"+str(nextPageCount)+DIR_URL
        
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
                        totalResultCount = self.parser.ParseTotalVehicleCount(page)
                        if totalResultCount is not None and totalResultCount >= 0:
                            tempCarLinks = self.parser.ParseCarLinks(siteDomain,page)
                            carLinksForASingleLink.extend(tempCarLinks)
                            while len(tempCarLinks) >= 50:
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
                        
                        
                        
            
            
            
            
            
            
            
    