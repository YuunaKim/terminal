
import datetime

import peewee 




db = peewee.SqliteDatabase('my_db.db')


class User(peewee.Model):
    first_name = peewee.CharField(max_length=255)
    last_name  = peewee.CharField(max_length=255)

    age = peewee.IntegerField()

    created_at = peewee.DateTimeField(default=datetime.datetime.now())

    

    class Meta:
        database = db

class Post(peewee.Model):
    title = peewee.CharField(max_length=255)  
    text = peewee.TextField()   

    author = peewee.ForeignKeyField(User, field='id')   

    created_at = peewee.DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db

db.connect()

db.create_tables([User, Post])





#CREATE TABLE user;
#CREATE TABLE posts;

# admin = User.create(first_name='admin', last_name='admin', age='42')

# post1= Post.create('Hello world', text='Lorem ipsum')


#\c my_db

# message1= '''
# +-------------------+
# | Welcome to my ORM |
# +-------------------+--------+
# | Enter 1 if you want to work|
# +----------------------------+
# '''
# message2 = '''
#     +-----------------------+
#     |   Choose model        |
#     +-----------------------+
#     |  1) User | 2)  Post   |
#     +-----------------------+
# '''

# while True:
#     print(message1)
#     a = input()
#     if a == '1':
#         print(message2)
#         a = input()
#         if a == '1':
#             first_name = input('\tEnter first_name')
#             last_name = input('\tEnter last_name')
#             age = int('input') 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