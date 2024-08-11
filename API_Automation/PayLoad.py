from Utilities.Configurations import getQuery
def Add_Book_Payload(isbn):
    body = {

        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": "227",
        "author": "John foe"
    }
    return body


def Build_Payload_From_DB(query):
    add_body = {}
    tp = getQuery(query)
    add_body['name'] = tp[0]
    add_body['isbn'] = tp[1]
    add_body['aisle'] = tp[2]
    add_body['author'] = tp[3]
    return add_body
