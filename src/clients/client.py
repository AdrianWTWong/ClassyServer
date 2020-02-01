import pycurl, json, io
import array as arr

#searchImage = input("Input image URL: ")
searchImage = "https://icdn2.digitaltrends.com/image/digitaltrends/galaxy-s10-plus-review-feat-768x479-c.jpg"
data = json.dumps({"image_url": searchImage})
url = 'http://localhost/search'

storage = io.BytesIO()

c = pycurl.Curl()
c.setopt(c.URL, str(url))
c.setopt(c.PORT, 3000)
c.setopt(c.HTTPHEADER, ['Content-Type: application/json'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, data)
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

returned_json = json.loads(storage.getvalue())

images = []
descriptions = []

for image in returned_json['links']:
    images.append(image)

for description in returned_json['links']:
    descriptions.append(description)

print(images)    
print(json.dumps(returned_json,indent=4))
