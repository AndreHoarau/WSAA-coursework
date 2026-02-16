# Author Andre Hoarau
# Writing a module to interact with api created by Andrew Beatty
# Test to make sure requests is working (it is )
'''import requests
url = 'http://google.com'
response = requests.get(url)
print(response.text)
'''
import requests
url = 'http://andrewbeatty1.pythonanywhere.com/books'
response = requests.get(url)
print(response.json())

def readbooks():
    response = response.json()
print(readbooks())