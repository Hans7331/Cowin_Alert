# -*- coding: utf-8 -*-
"""
Created on Tue May 11 00:56:04 2021

@author: hanst
"""

import time
import requests
from datetime import date
from beeply import notes
mybeep = notes.beeps(5000)

print("Enter District ID:")
district_id = int(input())
print("Enter Age limit (18,45):")
age_limit = int(input())


s=1

while(s!=0):
    try:
        time.sleep(30)
        r = date.today()
        r = str(r)
        r = r.split('-')
        r = r[::-1]
        r = r[0] + '-' + r[1] + '-' + r[2]
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        link = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id=" + str(district_id) + "&date=" + str(r)
        resp = requests.get(link,headers=headers)
        print(link)
        data = resp.json()
        data = data['centers']
        for hosp in data:
            hospe = hosp['sessions']
            for ses in hospe:
                if(ses['min_age_limit']==age_limit):
                    print(hosp['name'],'-',ses['date'], '-', ses['min_age_limit'], ses['vaccine'],'-', ses['available_capacity'])
                    if(ses['available_capacity']> 0):
                        mybeep.hear('C')
    except:
        print('API Down')