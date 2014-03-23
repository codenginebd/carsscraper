from bs4 import BeautifulSoup
class LandRoverParserTypeBad13:
    def __init__(self):
        pass
    
    def ParseCarLinks(self,baseUrl,page):
        carLinks = []
        try:
            soup = BeautifulSoup(page)
            carLinkContainerAnchorElements = soup.findAll("a",{"class":"fn url summary permalink"})
            for eachAnchor in carLinkContainerAnchorElements:
                carLink = baseUrl+eachAnchor["href"]
                carLinks.append(carLink)
        except Exception,exp:
            pass
        return carLinks
    
    def ParseTotalResultCount(self,page):
        resultCount = 0
        try:
            soup = BeautifulSoup(page)
            resultCountContainerElement = soup.find("span",{"class":"total-found"})
            if resultCountContainerElement is not None:
                resultCountText = resultCountContainerElement.text.strip()
                tempResultText = ""
                i = 0
                while resultCountText[i] >= "0" and resultCountText[i] <= "9":
                    tempResultText += resultCountText[i]
                    i += 1
                resultCount = int(tempResultText)
        except Exception,exp:
            resultCount = 0
        return resultCount
    
    def ExtractYearAndMakeModel(self,yearMakeModelText):
        yearMakeModel = {"title":yearMakeModelText}
        try:
            yearText = ""
            i = 0
            while yearMakeModelText[i] >= "0" and yearMakeModelText[i] <= "9":
                yearText += yearMakeModelText[i]
                i += 1
            if yearText != "":
                yearMakeModel["year"] = yearText
            makeModel = yearMakeModelText[len(yearText)+1:]
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
            priceContainerDivElement = soupObj.find("div",{"class":"price"})
            if priceContainerDivElement is not None:
                price = priceContainerDivElement.text.strip()
        except Exception,exp:
            pass
        return price
    
    def ParseCarInfo(self,soupObj):
        carInfo = {}
        try:
            infoDetailContainerElementDiv = soupObj.find("div",{"class":"vehicle-params"})
            if infoDetailContainerElementDiv is not None:
                infoContainerElementsRows = infoDetailContainerElementDiv.findAll("div",{"class":"row"})
                for eachRow in infoContainerElementsRows:
                    infoTitleElement = eachRow.find("div",{"class":"param"})
                    if infoTitleElement is not None:
                        infoTitleText = infoTitleElement.text.strip()
                        if infoTitleText is not None and infoTitleText != "":
                            if infoTitleText == "VIN #":
                                valueElement = eachRow.find("div",{"class":"value"})
                                if valueElement is not None and valueElement != "":
                                    carInfo["vin"] = valueElement.text.strip()
                            elif infoTitleText == "Exterior":
                                valueElement = eachRow.find("div",{"class":"value"})
                                if valueElement is not None:
                                    carInfo["exterior"] = valueElement.text.strip()
                            elif infoTitleText == "Interior":
                                valueElement = eachRow.find("div",{"class":"value"})
                                if valueElement is not None:
                                    carInfo["interior"] = valueElement.text.strip()
                            elif infoTitleText == "Year":
                                valueElement = eachRow.find("div",{"class":"value"})
                                if valueElement is not None:
                                    carInfo["year"] = valueElement.text.strip()
                            elif infoTitleText == "Make":
                                valueElement = eachRow.find("div",{"class":"value"})
                                if valueElement is not None:
                                    carInfo["make"] = valueElement.text.strip()
                            elif infoTitleText == "Model":
                                valueElement = eachRow.find("div",{"class":"value"})
                                if valueElement is not None:
                                    carInfo["model"] = valueElement.text.strip()
                            
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
            phoneNumberContainerSpanElement = soupObj.find("span",{"class":"number tel"})
            if phoneNumberContainerSpanElement is not None:
                phone = phoneNumberContainerSpanElement.text.strip()
        except Exception,exp:
            pass
        return phone
    
    def ParseCarDetails(self,link,state,page):
        carDetails = {"link":link,"state":state}
        try:
            soup = BeautifulSoup(page)
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
    
    
    