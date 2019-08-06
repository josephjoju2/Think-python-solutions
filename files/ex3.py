import anydbm
#works with python 2 not 3
db=anydbm.open('captions.db','c')

db['img1.jpg']='alcohol'
db['img2.jpg']='weed'

print(db['img1.jpg'])

for key,value in db.items():
    print(key+','+value)

db.close()
