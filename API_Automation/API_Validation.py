import requests
import json

response = requests.get('http://216.10.245.166//Library/GetBook.php', params={'AuthorName': 'Rahul Shetty'}, )
# print(response.text)
# print(type(response.text))
#
# books = json.loads(response.text)
# print(books[1]['book_name'])

json_response = response.json()
print(json_response)
print(type(json_response))
print(json_response[1]['book_name'])
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == "application/json;charset=UTF-8"

# Retrieve the book details with ISBN JH437

for Actual_book in json_response:
    if Actual_book['isbn'] == "JH437":
        print(Actual_book)
        break

Expected_Book = {
        "book_name": "Postman Testing",
        "isbn": "JH437",
        "aisle": "1234"
    }

assert Actual_book == Expected_Book