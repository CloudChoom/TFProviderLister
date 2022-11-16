import Constant
import Utils

providerResponse = Utils.GetTFProviders(Constant.START_PAGE, Constant.PAGE_SIZE) #Get the first page of providers and also learn how many pages there are in total

paginationDict = providerResponse["meta"]["pagination"]
totalPages = paginationDict["total-pages"]

with open("Output.txt", "w") as text_file:
    for currentPage in range(totalPages):
            providerResponse = Utils.GetTFProviders(str(currentPage+1), Constant.PAGE_SIZE)
            providerDict = providerResponse["data"]
            for item in providerDict:
                providerObject = item["attributes"]
                #Format: index,full-name,number of downloads,namespace
                print(providerObject["full-name"], ",", providerObject["downloads"], ",",providerObject["namespace"],",",providerObject["tier"],",",providerObject["source"],file=text_file)
                
print("DONE")


