import requests
from pprint import pprint

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def getHTML(link):
    headers = {
        "User-Agent" : "PostmanRuntime/7.26.5"
    }
    req = requests.get(link, headers=headers)
    html = str(req.content)
    return html

def getSeller(html):
    start = "chatUrl"
    end = "voucherListParams"
    block = find_between(html, start, end)
    name = find_between(block, "name\":\"", "\",") 
    url = find_between(block, "url\":\"", "\"},")
    print(name)
    print(url)
