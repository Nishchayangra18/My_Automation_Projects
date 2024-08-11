import requests
import configparser
from PayLoad import *
from Utilities.Configurations import *
from Utilities.resources import API_resources

Post_url = Get_Config()['API']['endpoint']+API_resources.add_Book
headers = {"Content-Type": "application/json"}
query = "select * from Books"
addBook_response = requests.post(Post_url, json=Build_Payload_From_DB(query), headers=headers, )

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

# Authentication
se = requests.session()    #Creates a session
se.auth = auth=('rahulshettyacademy', getPassword())

url = "https://api.github.com/user"
github_response = se.get(url)
print(github_response.status_code)