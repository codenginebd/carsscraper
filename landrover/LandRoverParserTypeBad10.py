from bs4 import BeautifulSoup
class LandRoverParserTypeBad10:
    def __init__(self):
        pass
    
    def ParseCarLinks(self,baseUrl,page):
        carLinks = []
        try:
            soup = BeautifulSoup(page)
            carLinkContainerH2Element = soup.findAll("h2",{"class":"vehicletitle"})
            for eachH2Element in carLinkContainerH2Element:
                carLinkAnchor = eachH2Element.find("a")
                if carLinkAnchor is not None:
                    carLink = carLinkAnchor["href"]
                    if carLink != "":
                        carLinks.append(baseUrl+carLink)
        except Exception,exp:
            pass
        return carLinks
    
    def ParseMakeModelYear(self,soupObj):
        makeModelYear = {}
        try:
            yearElement = soupObj.find("span",{"class":"year"})
            makeElement = soupObj.find("span",{"class":"make"})
            modelElement = soupObj.find("span",{"class":"model"})
            trimElement = soupObj.find("span",{"class":"trim"})
            if yearElement is not None:
                yearText = yearElement.text.strip()
                if yearText != "":
                    makeModelYear["year"] = yearText
            if makeElement is not None:
                makeText = makeElement.text.strip()
                trimText = ""
                if trimElement is not None:
                    trimText = trimElement.text.strip()
                if makeText != "":
                    if trimText != "":
                        make = makeText+" "+trimText
                        makeModelYear["make"] = make.strip()
                    else:
                        makeModelYear["make"] = makeText
                    
            if modelElement is not None:
                modelText = modelElement.text.strip()
                if modelText != "":
                    makeModelYear["model"] = modelText
        except Exception,exp:
            pass
        return makeModelYear
    
    def ParsePhone(self,soupObj):
        phone = None
        try:
            phoneElement = soupObj.find("span",{"class":"phonedata"})
            if phoneElement is not None:
                phone = phoneElement.text.strip()
        except Exception,exp:
            pass
        return phone
    
    def ParsePrice(self,soupObj):
        price = None
        try:
            priceListContainerDivElement = soupObj.find("div",{"id":"ctl00_ContentSection_ctl00_vi_pricing_pricing"})
            if priceListContainerDivElement is not None:
                priceListLis = priceListContainerDivElement.findAll("li")
                if priceListLis is not None:
                    prices = ""
                    for eachLi in priceListLis:
                        priceContainerSpanElement = eachLi.find("span")
                        if priceContainerSpanElement is not None:
                            prices += priceContainerSpanElement.text.strip() + ","
                    if prices != "":
                        price = prices[:-1]
        except Exception,exp:
            pass
        return price
    
    def ParseTotalVehicleCount(self,page):
        totalCount = None
        try:
            soup = BeautifulSoup(page)
            totalVehicleCountElement = soup.find("div",{"class":"recordCount"})
            if totalVehicleCountElement is not None:
                totalVehicleCountText = totalVehicleCountElement.text.strip()
                if totalVehicleCountText is not None and totalVehicleCountText != "":
                    countText = ""
                    i = 0
                    while totalVehicleCountText[i] >= "0" and totalVehicleCountText[i] <= "9":
                        countText += totalVehicleCountText[i]
                        i += 1
                    totalCount = int(countText)
        except Exception,exp:
            pass
        return totalCount
    
    def ParseCarInfo(self,soupObj):
        carInfo = {}
        try:
            carInfoDetailContainer = soupObj.find("div",{"class":"details"})
            carDetailsInfoListLis = carInfoDetailContainer.findAll("li")
            for eachLi in carDetailsInfoListLis:
                infoTitleElement = eachLi.find("label",{"class":"detailstitle"})
                infoDataElement = eachLi.find("span",{"class":"detailsinfo"})
                if infoTitleElement is not None and infoDataElement is not None:
                    infoTitleText = infoTitleElement.text.strip()
                    infoDataText = infoDataElement.text.strip()
                    if "Color:" in infoTitleText:
                        carInfo["exterior"] = infoDataText
                    elif "VIN:" in infoTitleText:
                        carInfo["vin"] = infoDataText
                    elif "Interior:" in infoTitleText:
                        carInfo["interior"] = infoDataText
        except Exception,exp:
            pass
        return carInfo
    
    def ParseCarDetails(self,link,state,page):
        carDetails = {"link":link,"state":state}
        try:
            soup = BeautifulSoup(page)
            carInfo = self.ParseCarInfo(soup)
            carDetails = dict(carDetails.items()+carInfo.items())
            price = self.ParsePrice(soup)
            if price is not None:
                carDetails["price"] = price
            phone = self.ParsePhone(soup)
            if phone is not None:
                carDetails["phone"] = phone
            makeModelYear = self.ParseMakeModelYear(soup)
            if makeModelYear is not None and type(makeModelYear) is dict:
                carDetails = dict(carDetails.items()+makeModelYear.items())
        except Exception,exp:
            pass
        return carDetails
    
    
    