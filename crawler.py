#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import re
import time

def myfilter(input):
    return not str.isdigit(input)

i = 1
data = {}

for i in range(1,598):
    time.sleep(5)
    url = 'https://www.futbin.com/21/players?page={}'.format(i)
    r = requests.get(url)
    print("Status: {}".format(r.status_code))
    print("Retry after: {}".format(r.headers))


    soup = BeautifulSoup(r.text, 'html.parser')

    if r.status_code == 200:
        for tr in soup.find_all('tr'):
            for td in tr.find_all('td'):
                for item in td.find_all('img'):
                    alt = item.get('alt')
                    data_original = item.get('data-original')

                    if (alt != None and alt != 'c' and data_original != None and data_original != 'c'):
                        name = ''.join(filter(myfilter, alt)).strip()
                        id = re.sub('\D', '', data_original.split('/')[7].split('.')[0])

                        data[name] = id
                        print(data[name])

with open('data.json', 'w') as f:
    json.dump(data, f)