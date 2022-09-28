from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# mongoDB에 넣은 데이터 중에서 '매트릭스'의 평점을 가져오기
movie = db.movies.find_one({'title':'매트릭스'},{'_id':False})
movie_score = movie['score']

# '매트릭스'의 평점과 같은 평점의 영화 제목들 가져오기
same_movies = list(db.movies.find({'score':movie_score},{'_id':False}))

for same in same_movies:
    print(same['title'])

# '매트릭스'영화의 평점을 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'score':'0'}})