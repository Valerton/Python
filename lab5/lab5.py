import numpy as np
import matplotlib.pylab as plt
from scipy import misc


img1 = misc.imread('photo.jpg')
plt.imshow(img1)
plt.show()

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15,5))

for c, ax in zip(range(3), axs):
    tmp_im = np.zeros(img1.shape, dtype="uint8")
    tmp_im[:,:,c] = img1[:,:,c]
    ax.imshow(tmp_im)
    ax.set_axis_off()
plt.show()

img1 = np.average(img1,weights = [0.2989, 0.5870, 0.1140],axis =2)


plt.imshow(img1, cmap=plt.cm.gray,vmin=10, vmax=100)
plt.show()