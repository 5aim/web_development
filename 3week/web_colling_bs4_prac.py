import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20220926',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#old_content > table > tbody > tr:nth-child(2) > td.title > div > a

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    if a_tag is not None:
        #old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        title = a_tag.text
        #old_content > table > tbody > tr:nth-child(2) > td.point
        score = tr.select_one('td.point').text

        doc = {
            'rank':rank,
            'title':title,
            'score':score
        }

        db.movies.insert_one(doc)