import requests
import json
from bs4 import BeautifulSoup

# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

def get_all():
    results = []

    file_path = './api/services/list_request.json'
    file = open(file_path, 'r')

    list_request = json.load(file)

    for query in list_request:
        result = get_by_name(query)
        if result:
            results.append(result)

    return results

def get_by_name(name):
    try:
        result = {}
        query = name.replace(' ', '+')
        URL = f"https://google.com/search?q={query}"

        headers = {"user-agent": USER_AGENT}
        resp = requests.get(URL, headers=headers)

        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")
            response = soup.find_all('span', jsname='vWLAgc')
            if response:
                value = response[0].text.replace(',','.')
                result = {'name':query, 'value': value}
                print(value)
    except:
        print(f"Ocorreu um error ao tentar consultar a ação: {query}")

    return result    
    