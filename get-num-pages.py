from scraper import Scraper
import bs4
from bs4 import BeautifulSoup
import requests
import json
from random import choice
headers = {
    '0': 'c', 
    '1': 'a',
    '2': 'l', 
    '3': 'l',
    '4': 'b',
    '5': 'a',
    '6': 'c',
    '7': 'k',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}   
csvheaders = ["Date",
                  "doc_number",
                  "DocumentTitle",
                  "PartyType",
                  "PartyName",
                  "Book",
                  "Page",
                  "LastISN",
                  "SearchResults"]

USER_AGENT_LIST = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0']
search_date = "20120201"
# we initialise a bot that will have run the parsing functions
headers.update({'User-Agent': choice(USER_AGENT_LIST)})
data = {
    "FirstName": "",
    "LastName": "",
    "MiddleInitial": "",
    "Suffix": "",
    "Organization": "",
    "Decade": "",
    "Year": "",
    "Date": search_date#,
    #"ContinueName": next_page_dict['continue_name'],
    #"ContinueDate": next_page_dict['continue_date'],
    #"ContinueRecordSequenceNumber": next_page_dict['continue_record_sequence_number'],
    #"ISN": next_page_dict['ISN']
}
post_url = 'https://erosi.saccounty.net/service/ERosi.svc/rest/PageSearch'
def getnextresult(next_page_dict):
    data = {
        "FirstName": "",
        "LastName": "",
        "MiddleInitial": "",
        "Suffix": "",
        "Organization": "",
        "Decade": "",
        "Year": "",
        "Date": search_date,
        "ContinueName": next_page_dict['continue_name'],
        "ContinueDate": next_page_dict['continue_date'],
        "ContinueRecordSequenceNumber": next_page_dict['continue_record_sequence_number'],
        "ISN": next_page_dict['ISN']
    }
    params = json.dumps(data)
    print(params)
    response = requests.post(post_url, data=params, headers=headers)
    print(response.json().keys())
    json_response = response.json()
    search_results = json_response['SearchResults']
    print(len(search_results))
    for value in json_response.values():
        if type(value) is list:
            for item in value:
                print(item.values())
                element_keys = []
                element_values = []
                for subitem1 in item:
                    subitem2 = item.get(subitem1)
                    if subitem1 in csvheaders:
                        element_keys.append(subitem1)
                        element_values.append(subitem2)


                elem = dict(zip(element_keys, element_values))

                print("elem")
                print(elem.get('ISN'))

    continue_name = elem.get('PartyName')
    continue_record_sequence_number = elem.get('Page')
    next_page_dict = {'ISN': elem.get('ISN'), 'continue_name': continue_name, 'continue_date': search_date, 'continue_record_sequence_number': continue_record_sequence_number}
    if(len(search_results) == 21):
       print("get next result")
       getnextresult(next_page_dict)
    else:
       exit()

continue_name = ""#result.get('PartyName')
continue_record_sequence_number = ""#result.get('Page')
nobel = Scraper("nobel", start_date="3/12/2017", end_date="3/12/2017", csvheaders=csvheaders)
params = json.dumps(data)
print(params)
response = requests.post(post_url, data=params, headers=headers)
print(response.json().keys())
json_response = response.json()
search_results = json_response['SearchResults']
print(len(search_results))
#for value in json_response.values():
   #print(type(value))
   #print(value)
   #if type(value) is list:
      #print(value)
      #for item in value:
         #print(item.keys())
#next_page_dict = {'ISN': elem.get('ISN'), 'continue_name': continue_name, 'continue_date': search_date, 'continue_record_sequence_number': continue_record_sequence_number}
for value in json_response.values():
   if type(value) is list:
      for item in value:
         print(item.values())
         element_keys = []
         element_values = []
         for subitem1 in item:
            subitem2 = item.get(subitem1)
            if subitem1 in csvheaders:
               element_keys.append(subitem1)
               element_values.append(subitem2)

         print(element_keys)
         print("element_keys")

         elem = dict(zip(element_keys, element_values))

         print("elem")
         print(elem.get('ISN'))
continue_name = elem.get('PartyName')
continue_record_sequence_number = elem.get('Page')
next_page_dict = {'ISN': elem.get('ISN'), 'continue_name': continue_name, 'continue_date': search_date, 'continue_record_sequence_number': continue_record_sequence_number}

if(len(search_results) == 21):
   print("get next result")
   getnextresult(next_page_dict)

