from bs4 import BeautifulSoup
class LandRoverParserTypeTom:
    def __init__(self):
        pass
    def ParseCarLinks(self,baseUrl,page):
        carLinks = []
        try:
            soup = BeautifulSoup(page)
            carLinksH1ElementList = soup.findAll("h1",{"class":"fn h3"})
            for eachCarLinkH1 in carLinksH1ElementList:
                if eachCarLinkH1 is not None:
                    linkAnchorElement = eachCarLinkH1.find("a",{"class":"url"})
                    if linkAnchorElement is not None:
                        carLinks.append(baseUrl+linkAnchorElement["href"])
        except Exception,exp:
            pass
        return carLinks
    
    def ParseLocationAndTelephone(self,soupObj):
        locationAndTel = {}
        try:
            locationContainerDivElement = soupObj.find("div",{"class":"ddc-content contact-info type-1"})
            if locationContainerDivElement is not None:
                locationTitleElement = locationContainerDivElement.find("span",{"class":"org"})
                if locationTitleElement is not None:
                    locationTitleText = locationTitleElement.text.strip()
                    locationAndTel["location"] = locationTitleText
                contactNumberContainerUL = locationContainerDivElement.find("ul",{"class":"tels"})
                if contactNumberContainerUL is not None:
                    phoneNumbers = []
                    contactNumberContainerLIs = contactNumberContainerUL.findAll("li",{"class":"tel phone1"})
                    for eachLi in contactNumberContainerLIs:
                        telephoneContainerElement = eachLi.find("span",{"class":"value"})
                        if telephoneContainerElement is not None:
                            telephoneNumber = telephoneContainerElement.text.strip()
                            phoneNumbers.append(telephoneNumber)
                    locationAndTel["phone"] = phoneNumbers
        except Exception,exp:
            pass
        return locationAndTel
    
    def ParseOverviewInfo(self,soupObj):
        overviewInfo = {}
        try:
            carOverviewInfoElement = soupObj.find("div",{"id":"overview"})
            if carOverviewInfoElement is not None:
                detailsListContainerElementUl = carOverviewInfoElement.find("ul",{"class":"details"})
                if detailsListContainerElementUl is not None:
                    exteriorColorLiElement = detailsListContainerElementUl.find("li",{"class":"exteriorColor"})
                    if exteriorColorLiElement is not None:
                        overviewInfo["exterior"] = exteriorColorLiElement.find("span",{"class":"value"}).text.strip()
                    interiorColorElement = detailsListContainerElementUl.find("li",{"class":"interiorColor"})
                    if interiorColorElement is not None:
                        overviewInfo["interior"] = interiorColorElement.find("span",{"class":"value"}).text.strip()
                    vinElement = detailsListContainerElementUl.find("li",{"class":"vin"})
                    if vinElement is not None:
                        overviewInfo["vin"] = vinElement.find("span",{"class":"value"}).text.strip()
        except Exception,exp:
            pass
        return overviewInfo
    
    def ParseTotalPageCount(self,page):
        pageCountTuple = None
        try:
            soup = BeautifulSoup(page)
            pageCountElement = soup.find("strong",{"class":"xsmall"})
            if pageCountElement is not None:
                pageCountText = pageCountElement.text.strip()
                ofIndex = pageCountText.find('of')
                if ofIndex != -1:
                    currentPageCountPart = pageCountText[:ofIndex]
                    totalPageCountPart = pageCountText[ofIndex:]
                    currentPageCountPart = currentPageCountPart.replace('Page','').strip()
                    totalPageCountPart = totalPageCountPart.replace('of','').strip()
                    pageCountTuple = (int(currentPageCountPart),int(totalPageCountPart))
        except Exception,exp:
            pass
        return pageCountTuple
    
    def ParseMSRP(self,soupObj):
        msrp = None
        try:
            priceElement = soupObj.find("strong",{"class":"h1 price"})
            if priceElement is not None:
                msrp = priceElement.text.strip()
        except Exception,exp:
            pass
        return msrp
    
    def ExtractYearAndMakeFromText(self,makeYearText):
        yearMakeModel = {"title":makeYearText}
        tempYear = ""
        for i in range(len(makeYearText)):
            if makeYearText[i] >= "0" and makeYearText[i] <= "9":
                tempYear += makeYearText[i]
            else:
                break
        make = "Land Rover"
        makeModel = makeYearText[len(tempYear):].strip()
        model = makeModel.replace(make,"")
        year = tempYear
        yearMakeModel["year"] = year
        yearMakeModel["make"] = make
        yearMakeModel["model"] = model
        return yearMakeModel
    
    def ParseMakeYear(self,soupObj):
        makeYear = {}
        try:
            makeYearContainerElement = soupObj.find("div",{"class":"ddc-content content-page-title "})
            if makeYearContainerElement is not None:
                makeYearText = makeYearContainerElement.find("h1").text.strip()
                yearMakeModel = self.ExtractYearAndMakeFromText(makeYearText)
                makeYear = yearMakeModel
        except Exception,exp:
            print exp
        return makeYear
    
    def ParseCarDetails(self,link,state,page):
        carDetails = {}
        carDetails["link"] = link
        carDetails["state"] = state
        try:
            soup = BeautifulSoup(page)
            overviewInfo = self.ParseOverviewInfo(soup)
            locationInfo = self.ParseLocationAndTelephone(soup)
            price = self.ParseMSRP(soup)
            makeYear = self.ParseMakeYear(soup)
            carDetails = dict(carDetails.items()+overviewInfo.items())
            carDetails = dict(carDetails.items()+locationInfo.items())
            carDetails = dict(carDetails.items()+makeYear.items())
            carDetails["price"] = price
        except Exception,exp:
            pass
        return carDetails