from bs4 import BeautifulSoup
class LandRoverParserTypeBad2:
    def __init__(self):
        pass
    
    def ParseCarLinks(self,baseUrl,page):
        carLinks = []
        try:
            soup = BeautifulSoup(page)
            carLinkContainerDivElements = soup.findAll("div",{"class":"itemTitleText"})
            for eachDiv in carLinkContainerDivElements:
                carLinkAnchor = eachDiv.find("a")
                if carLinkAnchor is not None:
                    carLink = baseUrl+carLinkAnchor["href"]
                    carLinks.append(carLink)
        except Exception,exp:
            pass
        return carLinks
    
    def ParsePageCount(self,page):
        pagecount = 0
        try:
            soup = BeautifulSoup(page)
            pageCountContainerDivElement = soup.find("div",{"class":"floatLeft fBold numVehiclesFoundNumber"})
            if pageCountContainerDivElement is not None:
                tempPagecount = pageCountContainerDivElement.text.strip()
                tempPagecount = tempPagecount.replace("&nbsp;","")
                pagecount = int(tempPagecount)
        except Exception,exp:
            pass
        return pagecount
    
    def ParsePagingLinks(self,page):
        links = []
        try:
            soup = BeautifulSoup(page)
            pageLinksContainerDivElement = soup.find("div",{"class":"activPage"})
            if pageLinksContainerDivElement is not None:
                linksAnchorList = pageLinksContainerDivElement.findAll("a")
                for eachAnchor in linksAnchorList:
                    links.append({"label":eachAnchor.text.strip(),"link":eachAnchor["href"].strip()})
        except Exception,exp:
            pass
        return links
    
    def ParseYearMakeModel(self,soupObj):
        yearMakeModel = None
        try:
            yearMakeModeElement = soupObj.find("div",{"class":"middleModelAndDescTop"})
            if yearMakeModeElement is not None:
                yearMakeModelText = yearMakeModeElement.text.strip()
                if yearMakeModelText != "":
                    yearMakeModel = self.ExtractYearAndMakeModel(yearMakeModelText)
        except Exception,exp:
            pass
        return yearMakeModel
    
    def ExtractYearAndMakeModel(self,yearMakeModelText):
        yearMakeModel = {"title":yearMakeModelText.strip()}
        try:
            yearText = ""
            i = 0
            while yearMakeModelText[i] >= "0" and yearMakeModelText[i] <= "9":
                yearText += yearMakeModelText[i]
                i += 1
            if yearText != "":
                yearMakeModel["year"] = yearText
            yearMakeModel["make"] = "Land Rover"
            yearMakeModel["model"] = yearMakeModelText.replace(yearText,"").replace("Land Rover","").strip()
        except Exception,exp:
            pass
        return yearMakeModel
    
    def ParseContactPhone(self,soupObj):
        phone = None
        try:
            phoneContainerDivElement = soupObj.find("div",{"class":"callUsContent"})
            if phoneContainerDivElement is not None:
                phoneDataContainerDiv = phoneContainerDivElement.find("div",{"class":"fs26 fBold btnTxtColor"})
                if phoneDataContainerDiv is not None:
                    phone = phoneDataContainerDiv.text.strip()
        except Exception,exp:
            pass
        return phone
    
    def ParsePrice(self,soupObj):
        price = None
        try:
            priceContainerDivElement = soupObj.find("div",{"itemprop":"price"})
            if priceContainerDivElement is not None:
                priceSpanElement = priceContainerDivElement.find("span")
                if priceSpanElement is not None:
                    priceText = priceSpanElement.text.strip()
                    if priceText != "" and priceText.startswith("$"):
                        price = priceText
        except Exception,exp:
            pass
        return price
    
    def ParseVIN(self,soupObj):
        vin = None
        try:
            vinContainerDivElement = soupObj.find("div",{"class":"mgb5"})
            if vinContainerDivElement is not None:
                vin = vinContainerDivElement.contents[2].strip()
        except Exception,exp:
            pass
        return vin
    
    def ParseCarInfo(self,soupObj):
        infoDetails = {}
        try:
            infoDetailContainerDivElement = soupObj.find("div",{"class":"detailControlWrapper"})
            if infoDetailContainerDivElement is not None:
                infoContainerDivElements = infoDetailContainerDivElement.findAll("div",{"class":"DescriptionColumnLabel"})
                for eachDiv in infoContainerDivElements:
                    infoTitle = eachDiv.text.strip()
                    if infoTitle == "Exterior Color:":
                        infoDataElement = eachDiv.nextSibling
                        infoDataElement = infoDataElement.nextSibling.nextSibling.nextSibling
                        if infoDataElement is not None:
                            infoDataText = infoDataElement.text.strip()
                            if infoDataText != "":
                                infoDetails["exterior"] = infoDataText
                    elif infoTitle == "Interior Surface:":
                        infoDataElement = eachDiv.nextSibling
                        infoDataElement = infoDataElement.nextSibling.nextSibling.nextSibling
                        if infoDataElement is not None:
                            infoDataText = infoDataElement.text.strip()
                            if infoDataText != "":
                                infoDetails["interior"] = infoDataText
        except Exception,exp:
            pass
        return infoDetails
    
    def ParseCarDetails(self,link,state,page):
        carDetails = {"link":link,"state":state}
        try:
            soup = BeautifulSoup(page)
            makeModelYear = self.ParseYearMakeModel(soup)
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
            vin = self.ParseVIN(soup)
            if vin is not None:
                carDetails["vin"] = vin
        except Exception,exp:
            pass
        return carDetails
    
    
    