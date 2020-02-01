import pycurl, json, io
import array as arr

#searchImage = input("Input image URL: ")
searchImage = "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mbp16-20191113-og?wid=1200&hei=630&fmt=jpeg&qlt=95&op_usm=0.5,0.5&.v=1573599067633"
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

for image in returned_json['links']:
    images.append(image)

print(images)    
#print(json.dumps(returned_json,indent=4))
