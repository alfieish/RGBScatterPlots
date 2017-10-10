from PIL import Image
import matplotlib.pyplot as plt
import random

piclocation = r'pathtofile.jpg'
im = Image.open(piclocation)

pixels = list(im.getdata())
pixel_sample = random.sample(pixels, 5000)

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

for i in pixel_sample:
    xs = i[0]
    ys = i[1]
    zs = i[2]
    r, g, b = xs/255, ys/255, zs/255
    c = (r, g, b)
    ax1.scatter(xs, ys, zs, c=c)

ax1.set_xlabel('Red Value')
ax1.set_ylabel('Green Value')
ax1.set_zlabel('Blue Value')

ax2 = fig.add_subplot(321)
ax2.imshow(im, interpolation='nearest')
ax2.axis("off")

plt.show()
