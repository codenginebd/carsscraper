from bs4 import BeautifulSoup
class LandRoverParserTypeBad5:
    def __init__(self):
        pass
    
    def ParseCarLinks(self,baseUrl,page):
        carLinks = []
        try:
            soup = BeautifulSoup(page)
            carLinkContainerH2Elements = soup.findAll("h2",{"class":"vName"})
            for eachH2 in carLinkContainerH2Elements:
                carLinkAnchor = eachH2.find("a")
                if carLinkAnchor is not None:
                    carLink = baseUrl+carLinkAnchor["href"]
                    carLinks.append(carLink)
        except Exception,exp:
            pass
        return carLinks
    
    def ParseTotalResultCount(self,page):
        resultCount = 0
        try:
            soup = BeautifulSoup(page)
            resultCountContainerElement = soup.find("span",{"class":"results-stats-ttl"})
            if resultCountContainerElement is not None:
                resultCountText = resultCountContainerElement.text.strip()
                resultCount = int(resultCountText)
        except Exception,exp:
            resultCount = 0
        return resultCount
    
    def ExtractYearAndMakeModel(self,yearMakeModelText):
        yearMakeModel = {"title":yearMakeModelText}
        try:
            temp = yearMakeModelText
            if temp.lower().startswith("new"):
                temp = yearMakeModelText[4:]
            yearText = ""
            i = 0
            while temp[i] >= "0" and temp[i] <= "9":
                yearText += temp[i]
                i += 1
            if yearText != "":
                yearMakeModel["year"] = yearText
            makeModel = temp[4+len(yearText)+1:]
            make = "Land Rover"
            model = makeModel.replace(make,"")
            yearMakeModel["make"] = make
            yearMakeModel["model"] = model
        except Exception,exp:
            pass
        return yearMakeModel
    
    def ParsePrice(self,soupObj):
        price = None
        try:
            priceListContainerUlElement = soupObj.find("ul",{"class":"vsrch_pricing"})
            if priceListContainerUlElement is not None:
                priceText = ""
                priceElementLis = priceListContainerUlElement.findAll("li")
                for eachLi in priceElementLis:
                    priceElementSpan = eachLi.find("span",{"class":"value"})
                    if priceElementSpan is not None:
                        tempPriceText = priceElementSpan.text.strip()
                        priceText += tempPriceText+","
                if priceText != "":
                    price = priceText[:-1]
        except Exception,exp:
            pass
        return price
    
    def ParseCarInfo(self,soupObj):
        carInfo = {}
        try:
            infoDetailContainerElementUL = soupObj.find("ul",{"id":"vInfoLst"})
            if infoDetailContainerElementUL is not None:
                infoContainerElementsLis = infoDetailContainerElementUL.findAll("li")
                for eachLI in infoContainerElementsLis:
                    infoTitleElement = eachLI.find("label")
                    if infoTitleElement is not None:
                        infoTitleText = infoTitleElement.text.strip()
                        infoDataText = eachLI.contents[1].strip()
                        if infoDataText is not None and infoDataText != "":
                            if infoTitleText == "Vin:":
                                carInfo["vin"] = infoDataText
                            elif infoTitleText == "Color Ext.:":
                                carInfo["exterior"] = infoDataText
                            elif infoTitleText == "Color Int.:":
                                carInfo["interior"] = infoDataText
                            elif infoTitleText == "Mileage:":
                                carInfo["mileage"] = infoDataText
                            
        except Exception,exp:
            pass
        return carInfo
    
    def ParseMakeModelYear(self,soupObj):
        makeModelYear = None
        try:
            makeModelYearElement = soupObj.find("div",{"id":"pg-vspecs-header"})
            if makeModelYearElement is not None:
                makeModelYearContainerH2Element = makeModelYearElement.find("h2")
                if makeModelYearContainerH2Element is not None:
                    makeModelYearText = makeModelYearContainerH2Element.text.strip()
                    makeModelYear = self.ExtractYearAndMakeModel(makeModelYearText)
        except Exception,exp:
            pass
        return makeModelYear
    
    def ParseContactPhone(self,soupObj):
        phone = None
        try:
            infoDetailsContainerDivElement = soupObj.find("div",{"id":"vData"})
            if infoDetailsContainerDivElement is not None:
                phoneContainerDiv = infoDetailsContainerDivElement.find("div",{"class":"tel"})
                if phoneContainerDiv is not None:
                    telDataContainerSpan = phoneContainerDiv.find("span",{"class":"value"})
                    if telDataContainerSpan is not None:
                        phone = telDataContainerSpan.text.strip()
        except Exception,exp:
            pass
        return phone
    
    def ParseCarDetails(self,link,state,page):
        carDetails = {"link":link,"state":state}
        try:
            soup = BeautifulSoup(page)
            makeModelYear = self.ParseMakeModelYear(soup)
            if makeModelYear is not None:
                carDetails = dict(carDetails.items()+makeModelYear.items())
            phone = self.ParseContactPhone(soup)
            if phone is not None:
                carDetails["phone"] = phone
            price = self.ParsePrice(soup)
            if price is not None:
                carDetails["price"] = price
            carInfo = self.ParseCarInfo(soup)
            carDetails = dict(carDetails.items()+carInfo.items())
        except Exception,exp:
            pass
        return carDetails
    
    
    