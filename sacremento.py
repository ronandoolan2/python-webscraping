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

continue_name = ""#result.get('PartyName')
continue_record_sequence_number = ""#result.get('Page')
nobel = Scraper("nobel", start_date="3/12/2017", end_date="3/12/2017", csvheaders=csvheaders)

#nobel = Scraper("nobel", start_date="3/12/2017", end_date="3/12/2017", delay=10)

url = "https://erosi.saccounty.net/#Results/{%22Type%22:%22Basic%22,%22Criteria%22:{%22FirstName%22:%22%22,%22LastName%22:%22%22,%22MiddleInitial%22:%22%22,%22Suffix%22:%22%22,%22Organization%22:%22%22,%22Decade%22:%22%22,%22Year%22:%22%22,%22Date%22:%22" + "20120201" + "%22}}"

post_url = 'https://erosi.saccounty.net/service/ERosi.svc/rest/PageSearch'
# we initialise a bot that will have run the parsing functions
#nobel = Scraper("nobel", start_date="3/12/2017", end_date="3/12/2017")
params = json.dumps(data)
print(params)
response = requests.post(post_url, data=params, headers=headers)
print(response.json())
def get_text(bs4_obj):
    print(bs4_obj)
    if isinstance(bs4_obj, bs4.element.NavigableString):
        return str(bs4_obj)
    elif isinstance(bs4_obj, bs4.element.Tag):
        print(bs4_obj.text)
        return bs4_obj.text
    else:
        return None


# below write the parsing functions for the data in the webpages for the webpage
@nobel.scrape(post_url, params=params)
def parse_page1():
    # We have the source of the page, let's ask BeaultifulSoup to parse it for
    # the bot
    print(type(nobel.response.json()))
    json_response = nobel.response.json()
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
             element_keys.append("Date")        
             element_values.append(search_date) 
             element_keys.append("doc_number")
             element_values.append(search_date[:4] + "-" + item.get("Book") + "&" + item.get("Page")) 
                     
             print(element_keys)
             print("element_keys")

             elem = dict(zip(element_keys, element_values))

             print("elem")
             print(elem.get('ISN'))
             continue_name = elem.get('PartyName')
             continue_record_sequence_number = elem.get('Page')#result.get('Page') 
             next_page_dict = {'ISN': elem.get('ISN'), 'continue_name': continue_name, 'continue_date': search_date, 'continue_record_sequence_number': continue_record_sequence_number}
             print(elem.get('PartyName'))
             yield elem
parse_functions = [parse_page1]

def get_other_pages(next_page_dict):
    post_url = 'https://erosi.saccounty.net/service/ERosi.svc/rest/PageSearch'
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

#@nobel.scrape(post_url, params=params)

# put the functions in a list where the sequence should be in the order that you
# want the bot to crawl through the pages
parse_functions = [parse_page1]
print(type(parse_functions))

# define the headers for the csv file that will be generated
nobel.headers = ["Date",
                  "doc_number",
                  "DocumentTitle",
                  "PartyType",
                  "PartyName",
                  "Book",
                  "Page"]

if __name__ == "__main__":
    nobel.run(parse_functions)
    print("hi")
