import requests
link = "https://csf101-server-cap1.onrender.com/get/input/347"
request_file = requests.get(link)
with open('347.txt', 'wb') as file:
    data = file.write(request_file.content)
print('Downloaded: 347.txt')