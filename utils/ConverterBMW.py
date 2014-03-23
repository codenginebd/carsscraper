import csv


class ConverterBMW:
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
        i = 0
        for eachDataRow in dataRows:
            i += 1
            eachDataRow = eachDataRow.strip()
            if eachDataRow != "":
                if self.CheckIfWebsite(eachDataRow) is True:
                    ###Now find address to split.
                    print records
                    address = records[1]
                    addressSplit = self.SplitAddress(address)
                    phoneNumber = records[2]
                    records.pop(2)
                    records.pop(1)
                    records.extend(addressSplit)
                    phoneNumber = phoneNumber.replace("Phone:","").strip()
                    records.append(phoneNumber)
                    records.append(eachDataRow.replace("Website:","").strip())
                    recordsList.append(records)
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
        
    def ConvertData(self):
        CSV_INPUT_FILE_NAME = "bmw.txt"
        dataRows = self.ReadFile(CSV_INPUT_FILE_NAME)
        records = self.SplitRecords(dataRows)
        self.WriteCSV("bmw_output.csv", records)

ConverterBMW().ConvertData()
            