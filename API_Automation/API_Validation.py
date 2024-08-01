import requests
import json

response = requests.get('http://216.10.245.166//Library/GetBook.php', params={'AuthorName': 'Rahul Shetty2'},)
# print(response.text)
# print(type(response.text))
#
# books = json.loads(response.text)
# print(books[1]['book_name'])

json_response = response.json()
print(json_response)
print(type(json_response))
print(json_response[1]['book_name'])