from pymongo import MongoClient
from pprint import pprint
import json

# Подключение к MongoDB
client= MongoClient(host='localhost', port=27017)
# Создание базы данных
db = client['bookstore']
# Создание коллекции
collection = db['books']

# Загрузка данных JSON из файла
with open('books.json') as file:
    data = json.load(file)

# Вставка данных в коллекцию
    collection.insert_many(data)

print('Данные загружены')

# Запрос на книги не дороже 100:
expensive_books = collection.find({"price": {"$lte": 100}})
for book in expensive_books:
    print(book)

# Запрос на книги, количество которых больше 10:
popular_books = collection.find({"availability": {"$gt": 10}})
for book in popular_books:
    print(book)