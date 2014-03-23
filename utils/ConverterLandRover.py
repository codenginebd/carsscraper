import csv


class ConverterLandRover:
    def __init__(self):
        pass
    
    def ReadCSV(self,CSV_FILE_NAME):
        dataRows = []
        with open(CSV_FILE_NAME, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for eachRow in reader:
                if eachRow is not None and eachRow != "":
                    dataRows.append(eachRow)
        return dataRows
    
    def ReadFile(self,FILE_NAME):
        f = open(FILE_NAME,"r")
        contents = f.readlines()
        f.close()
        return contents
    
    def CheckIfTelephoneNumber(self,data):
        data = data.strip()
        temp = data
        if data.startswith("Phone:"):
            temp = data.replace("Phone:","")
        
        if temp != "":
            for i in temp:
                if (i >= "0" and i <= "9") or i == "-" or i == "." or i == "(" or i == ")" or i == " ":
                    continue
                else:
                    return False
        else:
            return False
        return True
    
    def CheckIfWebsite(self,data):
        if data.startswith("Website:"):
            return True
        else:
            return False
    
    def SplitAddress(self,address):
        address = address.replace("\"","")
        addresArray = []
        addressSplit = address.split(",")
        addresArray.append(addressSplit[0])
        addresArray.append(addressSplit[1])
        addresArray.append(addressSplit[2])
        addresArray.append(addressSplit[3])
        return addressSplit
            
    
    def SplitRecords(self,dataRows):
        recordsList = []
        records = []
        for eachDataRow in dataRows:
            eachDataRow = eachDataRow.strip()
            if eachDataRow == "":
                companyTitle = records[0].strip()
                address = records[1].strip()
                addressSplit = address.split(",")
                phone ,fax, email = "","",""
                if len(records) > 2:
                    title = records[2].strip()
                    if title.startswith("Phone"):
                        if len(records) > 3:
                            phone = "Phone: "+records[3]
                if len(records) > 4:
                    title = records[4].strip()
                    if title.startswith("Fax"):
                        if len(records) > 5:
                            fax = "Fax: "+records[5]
                if len(records) > 6:
                    title = records[6].strip()
                    if title.startswith("Email"):
                        if len(records) > 7:
                            email = "Email: "+records[7]
                tempRecords = []
                tempRecords.append(companyTitle)
                tempRecords.append(addressSplit[0])
                tempRecords.append(addressSplit[1])
                tempRecords.append(addressSplit[2])
                tempRecords.append(addressSplit[3])
                tempRecords.append(phone)
                tempRecords.append(fax)
                tempRecords.append(email)
                recordsList.append(tempRecords)
                records = []
            else:
                records.append(eachDataRow)
        return recordsList
    
    def WriteCSV(self,FILE_NAME,dataRows):
        csvFile = open(FILE_NAME,"wb")
        csvFile.close()
        csvFile = open(FILE_NAME,"ab")
        csvWritter = csv.writer(csvFile)
        for eachDataRow in dataRows:
            csvWritter.writerow(eachDataRow)
        csvFile.close()
        
    def FormatTextFile(self,dataRows):
        f = open("landRover_input.txt","wb")
        for eachRow in dataRows:
            if eachRow.strip() != "":
                f.write(str(eachRow))
        f.close()
        
    def ConvertData(self):
        CSV_INPUT_FILE_NAME = "landRover_input.txt"
        dataRows = self.ReadFile(CSV_INPUT_FILE_NAME)
#        self.FormatTextFile(dataRows)
        records = self.SplitRecords(dataRows)
        self.WriteCSV("landRover_output.csv", records)

ConverterLandRover().ConvertData()
            