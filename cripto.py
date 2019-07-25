import requests

url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
my_token = '4646090ebb3fd4037ecb08134825732b36e73e84'

response = requests.get(url, params={'token': my_token})
json_response = response.json()
print(json_response)

