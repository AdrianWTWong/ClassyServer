import requests, json

url = "http://localhost:5000/search"

data = {
    "image_url":"https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg",
    "resized_images":True # Or true
}


headers = {'Content-type': 'application/json'}
r = requests.post(url, headers=headers, data=json.dumps(data))

#r.json to get the response as json
print(r.json())
