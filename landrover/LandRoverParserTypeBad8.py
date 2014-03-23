from bs4 import BeautifulSoup
class LandRoverParserTypeBad8:
    def __init__(self):
        pass
    def ParseCarLink(self,baseUrl,soupElement):
        carsLink = None
        try:
            carLinkContainerAnchorElement = soupElement.find("a",{"class":"view-more-info btn-lg"})
            if carLinkContainerAnchorElement is not None:
                carLinksHref = carLinkContainerAnchorElement["href"]
                if carLinksHref is not None and carLinksHref != "":
                    carsLink = baseUrl+carLinksHref
        except Exception,exp:
            pass
        return carsLink
    
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
    
    def ParsePrice(self,siteDomain,soupElement):
        price = None
        try:
            if "landroverftlauderdale" in siteDomain or "landroverencino" in siteDomain:
                priceContainerElement = soupElement.find("div",{"class":"smartChoicePrice"})
                if priceContainerElement is not None:
                    price = priceContainerElement.text.replace("*","").strip()
            elif "landroverboise" in siteDomain:
                priceContainerElement = soupElement.find("span",{"class":"price"})
                if priceContainerElement is not None:
                    price = priceContainerElement.text.replace("*","").strip()
        except Exception,exp:
            print exp
        return price
    
    def ParseContactPhone(self,soupObj):
        contactPhone = None
        try:
            contactPhoneContainerElement = soupObj.find("h1",{"class":"PhoneNumber"})
            if contactPhoneContainerElement is not None:
                contactPhone = contactPhoneContainerElement.text.strip()
        except Exception,exp:
            print exp
        return contactPhone
    
    def ParseTotalPageCount(self,page):
        pageCountTuple = None
        try:
            soup = BeautifulSoup(page)
            pageCountElement = soup.find("div",{"id":"inventory-pager-summary"})
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
    
    def ParseCarDetails(self,siteDomain,state,page):
        carDetailsList = []
        try:
            soup = BeautifulSoup(page)
            phone = self.ParseContactPhone(soup)
            carListContainerElement = soup.find("ul",{"id":"results-list-detail"})
            if carListContainerElement is not None:
                carListLis = carListContainerElement.findAll("li")
                for eachLi in carListLis:
                    carDetails = {"state":state}
                    if phone is not None and phone != "":
                        carDetails["phone"] = phone
                    infoContainerElement = eachLi.find("div",{"class":"vehicle-info"})
                    priceContainerElement = eachLi.find("div",{"class":"price-cta"})
                    if infoContainerElement is not None:
                        yearMakeContainerElement = infoContainerElement.find("h6")
                        if yearMakeContainerElement is not None:
                            yearMakeText = yearMakeContainerElement.text.strip()
                            yearMakeModel = self.ExtractYearAndMakeFromText(yearMakeText)
                            carDetails = dict(carDetails.items()+yearMakeModel.items())
                        ###Now need to find out car details.
                        dtElements = infoContainerElement.findAll("dt")
                        ddElements = infoContainerElement.findAll("dd")
                        if dtElements is not None and ddElements is not None and type(dtElements) is list and type(ddElements) is list:
                            if len(dtElements) == len(ddElements):
                                for i in range(len(dtElements)):
                                    titleElement = dtElements[i]
                                    dataElement = ddElements[i]
                                    titleText = titleElement.text.strip()
                                    dataText = dataElement.text.strip()
                                    if titleText.startswith("Int."):
                                        carDetails["interior"] = dataText
                                    elif titleText.startswith("Ext."):
                                        carDetails["exterior"] = dataText
                                    elif titleText.startswith("VIN:"):
                                        carDetails["vin"] = dataText
                        
                    if priceContainerElement is not None:
                        price = self.ParsePrice(siteDomain, priceContainerElement)
                        if price is not None and price != "":
                            carDetails["price"] = price
                        carDetailLink = self.ParseCarLink(siteDomain, priceContainerElement)
                        if carDetailLink is not None and carDetailLink != "":
                            carDetails["link"] = carDetailLink
                    carDetailsList.append(carDetails)
        except Exception,exp:
            print exp
        return carDetailsList