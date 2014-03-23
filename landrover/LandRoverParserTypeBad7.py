from bs4 import BeautifulSoup
class LandRoverParserTypeBad7:
    def __init__(self):
        pass
    def ParseCarLinks(self,baseUrl,page):
        carsLinks = []
        try:
            soup = BeautifulSoup(page)
            carLinksContainerH4Elements = soup.findAll("h4")
            for eachH4 in carLinksContainerH4Elements:
                carLinksAnchorelement = eachH4.find("a")
                if carLinksAnchorelement is not None:
                    carLinksHref = carLinksAnchorelement["href"]
                    carsLinks.append(baseUrl+carLinksHref)
        except Exception,exp:
            pass
        return carsLinks
    
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
    
    def ParseYearMake(self,soupObj):
        yearMake = {}
        try:
            yearMakeContainerElement = soupObj.find("h1",{"id":"vehicle_title"})
            if yearMakeContainerElement is not None:
                yearMakeText = yearMakeContainerElement.text.strip()
                yearMakeModel = self.ExtractYearAndMakeFromText(yearMakeText)
                yearMake = yearMakeModel
        except Exception,exp:
            print exp
        return yearMake
    
    def ParsePrice(self,soupObj):
        price = None
        try:
            priceContainerElement = soupObj.find("li",{"class":"price_line_1"})
            if priceContainerElement is not None:
                price = priceContainerElement.text.strip()
        except Exception,exp:
            print exp
        return price
    
    def ParseCarInfo(self,soupObj):
        carInfo = {}
        try:
            infoContainerElement = soupObj.find("div",{"id":"vitalsContainer"})
            if infoContainerElement is not None:
                infoRowsLis = infoContainerElement.findAll("li")
                for eachLi in infoRowsLis:
                    infoTitleContainerElement = eachLi.find("strong")
                    if infoTitleContainerElement is not None:
                        infoTitle = infoTitleContainerElement.text.strip()
                        infoData = eachLi.contents[1].strip()
                        if infoTitle == "Exterior:":
                            carInfo["exterior"] = infoData
                        elif infoTitle == "Interior:":
                            carInfo["interior"] = infoData
                        elif infoTitle == "VIN #:":
                            carInfo["vin"] = infoData
        except Exception,exp:
            pass
        return carInfo
    
    def ParseContactPhone(self,soupObj):
        contactPhone = None
        try:
            contactPhoneContainerElement = soupObj.find("div",{"id":"vehicle_contact"})
            if contactPhoneContainerElement is not None:
                contactElementSpan = contactPhoneContainerElement.find("span")
                if contactElementSpan is not None:
                    contactPhone = contactElementSpan.text.strip()
        except Exception,exp:
            print exp
        return contactPhone
    
    def ParseCarDetails(self,link,state,page):
        carDetails = {"link":link,"state":state}
        try:
            soup = BeautifulSoup(page)
            yearMake = self.ParseYearMake(soup)
            carDetails = dict(carDetails.items()+yearMake.items())
            phone = self.ParseContactPhone(soup)
            if phone is not None:
                carDetails["phone"] = phone
            price = self.ParsePrice(soup)
            if price is not None:
                carDetails["price"] = price
            carInfo = self.ParseCarInfo(soup)
            carDetails = dict(carDetails.items()+carInfo.items())
        except Exception,exp:
            print exp
        return carDetails