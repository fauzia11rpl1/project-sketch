# library numpy -> pip install numpy
# library imageio -> pip install imageio
# library scipy -> pip install scipy
# library opency -> pip install opency-python
# kita pakai library image yang kemarin (pip install image)
# siapkan 1 gambar di folder yg sama untuk diconvert menjadi sketsa pensii

# import library yg akan digunakan
import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "ayangku.jpg" # nama file input

def rgb2gray(rgb):
  return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])
# formula untuk convert img -> grayscale // pakai kode warna matlab

def dodge(front,back):
  final_sketch = front*255/(255-back)
  #kalau gambarnya lebih besar dari 255 bit/ps maka akan diconvert jadi 255
  final_sketch [final_sketch>255]=255
  final_sketch [back==255]=255

  return final_sketch.astype('uint8')

# untuk read gambar yg dipilih
SS = imageio.imread(img) # untuk read gambar yg dipilih awal tadi
gray = rgb2gray(SS) # untuk convert gambar jadi black and white

i = 255-gray

# untuk memberi efek blur 
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)
# sigma=15 adalah itensitas blurnya

r = dodge(blur,gray)
# untuk convert gambarnya (dngn mengaplikasikan blur & black&white tadi)

cv2.imwrite("sketsa.png", r)
# untuk menghasilkan output gambar bernama sketsa.png
# run > start debugging
