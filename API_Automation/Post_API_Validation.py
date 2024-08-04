import requests
import configparser
from PayLoad import *
from Utilities.Configurations import *
from Utilities.resources import API_resources

Post_url = Get_Config()['API']['endpoint']+API_resources.add_Book
headers = {"Content-Type": "application/json"}
addBook_response = requests.post(Post_url, json=Add_Book_Payload("jqwert"), headers=headers, )

print(addBook_response.json())
response_json = addBook_response.json()
book_ID = response_json['ID']

# Delete book -
Delete_url = Get_Config()['API']['endpoint']+API_resources.delete_Book
response_deleteBook = requests.post(Delete_url, json=
{
    "ID": book_ID
}, headers={"Content-Type": "application/json"}, )

assert response_deleteBook.status_code == 200
delete_response_json = response_deleteBook.json()
assert delete_response_json['msg'] == "book is successfully deleted"
