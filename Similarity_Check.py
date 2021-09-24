from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pandas as pd
import json
from bs4 import BeautifulSoup
import re 
from urllib.request import urlopen
import requests
import time


def get_similarity(contract):
    url = 'http://192.168.128.142:9000/'
    data = {'code' : contract}

    response = requests.post(url,data=data)
    #print(response.text)
    time.sleep(1)
    soup = BeautifulSoup(response.text, 'html.parser')
    similarity = str(soup.find_all('h1')[2])
    similarity=re.sub('<.+?>', '', similarity, 0).strip()
    print(similarity)
    return similarity

def get_contract(data):
    
    token = 'VFQIHCD19UDTRRDQUYF19HZK3QS1Y8ZXBF'
    line = data['platform.token_address']
    repos_url = 'https://api.etherscan.io/api?module=contract&action=getsourcecode&address='+line+'&apikey='+token
    #print(repos_url)
    gh_session = requests.Session()
    repos = json.loads(gh_session.get(repos_url).text)
    contract = repos['result'][0]['SourceCode']
    #print(contract[-20:])
    try:
        similarity = get_similarity(contract)
    #    print(similarity)
    except:
        print("check this contract : " + repos_url)
    gh_session.close()
#   

if __name__=='__main__':
    csv_test = pd.read_csv('total_v1.1.csv')
    datas = csv_test.to_dict('records')
    token = 'VFQIHCD19UDTRRDQUYF19HZK3QS1Y8ZXBF'

    for data in datas:
        get_contract(data)





#for data in datas:
#    line = data['platform.token_address']       
#    print (line)
#    repos_url = 'https://api.etherscan.io/api?module=contract&action=getsourcecode&address='+line+'&apikey='+token
#    gh_session = requests.Session()
#    repos = json.loads(gh_session.get(repos_url).text) # json으로 뽑아오자
#    contract = repos['result'][0]['SourceCode']
#    similarity = get_similarity(contract)
#    print(similarity)
#    gh_session.close()
#    print(repos.keys())
#    for source in repos['result']:
#        time.sleep(0.5)
#        print(source['SourceCode'])