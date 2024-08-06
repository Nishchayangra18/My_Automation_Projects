import requests

cookie = {'visit-month': 'February'}
response = requests.get('https://rahulshettyacademy.com', allow_redirects=False, cookies=cookie, timeout=1)
print(response.history)  # This gives us the information about any redirection before opening the specified url.
print(response.status_code)

se = requests.session()
se.cookies.update(cookie)

res = se.get('https://httpbin.org/cookies', cookies={'visit-year': '1998'})
print(res.text)
print(res.status_code)

# Attachments

url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('C:\\Users\\Nishchay\\Downloads\\BD62BCF9-B29A-4336-8A74-558B800731FD.png', 'rb')}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)
