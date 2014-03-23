import csv


class ConverterMarcedes:
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
        if data != "":
            for i in data:
                if (i >= "0" and i <= "9") or i == "-" or i == "." or i == "(" or i == ")" or i == " ":
                    continue
                else:
                    return False
        else:
            return False
        return True
    
    def SplitAddress(self,address):
        address = address.replace("\"","")
        addressSplit = []
        addressArray = address.split(",")
        if len(addressArray) > 1:
            addressSplit.append(addressArray[0])
            remainingPart = addressArray[1]
            zip = ""
            for i in range(len(remainingPart)):
                if remainingPart[len(remainingPart) - 1 - i] >= "0" and remainingPart[len(remainingPart) - 1 - i] <= "9":
                    zip += remainingPart[len(remainingPart) - 1 - i]
                else:
                    break
            if zip != "":
                state = remainingPart[:len(remainingPart)-len(zip)].strip()
                if state != "":
                    addressSplit.append(state)
                    addressSplit.append(zip[::-1])
        return addressSplit
            
    
    def SplitRecords(self,dataRows):
        recordsList = []
        records = []
        i = 0
        for eachDataRow in dataRows:
            i += 1
            eachDataRow = eachDataRow.strip()
            if eachDataRow != "":
                if self.CheckIfTelephoneNumber(eachDataRow) is True:
                    ###Now find address to split.
                    address = records[len(records) - 1]
                    addressSplit = self.SplitAddress(address)
                    records.pop(len(records) - 1)
                    records.extend(addressSplit)
                    records.append(eachDataRow)
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
        CSV_INPUT_FILE_NAME = "mercedes.csv"
        dataRows = self.ReadFile(CSV_INPUT_FILE_NAME)
        records = self.SplitRecords(dataRows)
        self.WriteCSV("mercedes_output.csv", records)

ConverterMarcedes().ConvertData()
            