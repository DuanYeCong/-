from PIL import Image
import os
import glob
  
path = r'picTemp/*.png'
for i in glob.glob(path):
  im1 = Image.open(i)
  im2 = im1.resize((512,512))
  im2.save(os.path.join(r'picTemp',os.path.basename(i)))
  print('正在生成：',i)
print('finish')