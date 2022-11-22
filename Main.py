import Constant
import Utils

providerResponse = Utils.GetTFProviders(Constant.START_PAGE, Constant.PAGE_SIZE) #Get the first page of providers and also learn how many pages there are in total

paginationDict = providerResponse["meta"]["pagination"]
totalPages = paginationDict["total-pages"]

count = 1

with open("Output.txt", "w") as text_file:
    for currentPage in range(totalPages):
            providerResponse = Utils.GetTFProviders(str(currentPage+1), Constant.PAGE_SIZE)
            providerDict = providerResponse["data"]
            for item in providerDict:
                providerObject = item["attributes"]
                Provider_Id = item["id"]

                DownloadSummaryResponse = Utils.GetProviderDownloadSummary(Provider_Id)
                DownloadSummaryDict = DownloadSummaryResponse["data"]["attributes"]

                TotalDownloads = str(DownloadSummaryDict["total"])
                YearlyDownloads = str(DownloadSummaryDict["year"])
                MonthlyDownloads = str(DownloadSummaryDict["month"])
                WeeklyDownloads = str(DownloadSummaryDict["week"])

                print(str(count), "/", str(paginationDict["total-count"]))
                
                count+=1

                #Format: provider id,full-name, yearly downloads, monthly downloads, weekly downloads, Total Downloads, namespace
                #print(item["id"],",",providerObject["full-name"], ",", YearlyDownloads, ",",MonthlyDownloads, ",",WeeklyDownloads, ",",TotalDownloads, ",",providerObject["namespace"],",",providerObject["tier"],",",providerObject["source"])
                print(item["id"],",",providerObject["full-name"], ",", YearlyDownloads, ",",MonthlyDownloads, ",",WeeklyDownloads, ",",TotalDownloads, ",",providerObject["namespace"],",",providerObject["tier"],",",providerObject["source"],file=text_file)
                
print("DONE")


