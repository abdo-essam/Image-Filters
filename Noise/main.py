import cv2
from scipy import signal
#from scipy import skimage
import matplotlib.pyplot as plt #
from skimage.util import random_noise
from scipy import ndimage, misc
import matplotlib.pyplot as plt
from skimage.data import camera
from skimage.filters import threshold_local
import matplotlib.pyplot as plt


normal = cv2.imread(r'D:\lena.png',0)
noisy =  cv2.imread(r'D:\noisy.png',0)



fig=plt.figure(figsize=(16, 16)) #
fig.add_subplot(4, 4, 1)
plt.title('Original')
plt.imshow(normal,cmap = 'gray') #grayscale

fig.add_subplot(4, 4, 2)
plt.title('Gaussian')
gaussian = random_noise(normal,  mode='gaussian', seed=None, clip=True)
plt.imshow(gaussian,cmap = 'gray')



fig.add_subplot(4, 4, 3)
plt.title('Original')
plt.imshow(noisy,cmap = 'gray') #grayscale

fig.add_subplot(4, 4, 4)
plt.title('Wiener')
wiener = signal.wiener(noisy,(1,1))
plt.imshow(wiener,cmap = 'gray')



fig.add_subplot(4, 4,5)
plt.title('Original')
plt.imshow(normal,cmap = 'gray') #grayscale

fig.add_subplot(4, 4, 6)
plt.title('Salt & Pepper')
sp = random_noise(normal,  mode='s&p', seed=None, clip=True)
plt.imshow(sp ,cmap = 'gray') #grayscale



fig.add_subplot(4, 4, 7)
plt.title('Original')
plt.imshow(normal,cmap = 'gray') #grayscale

fig.add_subplot(4, 4, 8)
plt.title('Mean')
mean = threshold_local(normal, block_size=15, method='mean', offset=0, mode='reflect', param=None, cval=0)
plt.imshow(mean ,cmap = 'gray') #grayscale



fig.add_subplot(4, 4,9)
plt.title('Original')
plt.imshow(normal,cmap = 'gray') #grayscale

fig.add_subplot(4, 4, 10)
plt.title('Median')
median = threshold_local(normal, block_size=15, method='median', offset=0, mode='reflect', param=None, cval=0)
plt.imshow(median ,cmap = 'gray') #grayscale



fig = plt.figure()
plt.gray()  # show the filtered result in grayscale
ax1 = fig.add_subplot(121)  # left side
ax2 = fig.add_subplot(122)  # right side
ascent = misc.ascent()
result = ndimage.minimum_filter(ascent, size=20)
ax1.imshow(ascent)
ax2.imshow(result)
plt.show()



fig = plt.figure()
plt.gray()  # show the filtered result in grayscale
ax1 = fig.add_subplot(121)  # left side
ax2 = fig.add_subplot(122)  # right side
ascent = misc.ascent()
result = ndimage.maximum_filter(ascent, size=20)
ax1.imshow(ascent)
ax2.imshow(result)
plt.show()