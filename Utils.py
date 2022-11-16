import json
import urllib3
import Constant

def GetTFProviders(pageNumber, pageSize):
    url = Constant.BASE_URL + "/v2/providers?filter[tier]=official,partner,community&page[number]=" + pageNumber + "&page[size]="+ pageSize +"&sort=-featured,tier,name"
    response = urllib3.PoolManager().request("GET", url, headers={'Content-Type': 'application/json'})
    provider_response = json.loads(response.data.decode("utf-8"))

    return provider_response