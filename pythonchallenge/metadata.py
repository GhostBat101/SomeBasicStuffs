from PIL import Image
from PIL.ExifTags import TAGS

imagename = "20210206_214344.jpg"
image = Image.open(imagename)

edata = image.getexif()

for tag_id in edata:
    tag = TAGS.get(tag_id, tag_id)
    data = edata.get(tag_id)
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")