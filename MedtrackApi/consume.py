import requests

response = requests.get('http://127.0.0.1:8000/Patient/')
print (response.json())




# import requests

# url = 'http://127.0.0.1:8000/Patient'
# response = requests.get(url)

# json_data = response.json()

# print (json_data)
