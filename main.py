import os
from PIL import Image

dirname = 'D:\\Username\\Folder'
picdir = dirname+'\\Pictures'
dir = os.listdir(dirname)

list = [Image.open(picdir+'\\'+i).convert("RGB") for i in os.listdir(picdir) if i.endswith(".jpg")]
print(list)

Image.open(dirname+'\\save.jpg').convert("RGB").save(dirname+'\\output.pdf', "PDF" ,resolution=100.0, save_all=True, append_images=list)
