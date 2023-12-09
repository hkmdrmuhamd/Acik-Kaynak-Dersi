import requests
URL="https://www.fruityvice.com/api/fruit/apple"
result=requests.get(URL)
data=result.json()
print(data)
