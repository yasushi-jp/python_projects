# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 23:44:00 2019

@author: yasushi
"""

import requests
import json

url = 'https://qiita.com/api/v2/authenticated_user/items'
params = { "page" : "1", "per_page" : "100"}
headers = {"content-type" : "application/json", "Authorization" : "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
res = requests.get(url, headers=headers, params=params)
list = res.json()

total_views_cnt = 0
total_likes_cnt = 0
total_stocks_cnt = 0

print("作成日,タイトル,URL,ビューカウント,いいねカウント,ストックカウント")
for item in list:
    item_id = item['id']
    title = item['title']
    likes_cnt = item['likes_count']
    create_date = item['created_at']
    item_url = item['url']

    total_likes_cnt += likes_cnt

    url = 'https://qiita.com/api/v2/items/' + item_id
    res = requests.get(url, headers=headers)
    json = res.json()
    views_cnt = json['page_views_count']
    total_views_cnt += views_cnt

    url = 'https://qiita.com/api/v2/items/' + item_id + '/stockers'
    res = requests.get(url, headers=headers)
    users = res.json()
    stocks_cnt = len(users)
    total_stocks_cnt += stocks_cnt

    print(create_date + ", " + title + ", " + item_url + ", " + str(views_cnt) + ", " + str(likes_cnt) + ", " + str(stocks_cnt))
    
print("合計, , , " + str(total_views_cnt) + ", " + str(total_likes_cnt) + ", " + str(total_stocks_cnt))
