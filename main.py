import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

image_loc = "1.jpg" # Change image location

def find_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)
    hist = hist.astype("float")
    hist /= hist.sum()

    return hist
def plot_colors2(hist, centroids):
    bar = np.zeros((100, 500,3), dtype="uint8")
    startX = 0
    ans={}
    neutral=0
    for (percent, color) in zip(hist, centroids):
        ans[percent*100] = matplotlib.colors.to_hex(color/255)
        endX = startX + (percent * 500)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 100),color.astype("uint8").tolist(), -1)
        startX = endX
    print("Top dominating colours are :")
    print('  HexCode Percentage')
    i=1        
    for p in reversed(sorted(ans)):
        if ans[p] == '#000000':# neutral colors
            neutral = p
            continue
        print(i,ans[p],'{:f}'.format(p))
        i = i+1
    print("Image contains",neutral,"% of neutral colors.")
    print("Note: Black color on histogram represents neutral colors.")
    # return the bar chart
    return bar

img = cv2.imread(image_loc)
# To remove neutral colors, I converted image to HSV format,
# as removing a range of values is difficult in RGB format.
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# By trail-error metod i decided this bounds. 
lower = np.array([0,25,40])       
upper = np.array([180,255,255])
# Removing neutral colors from image
mask = cv2.inRange(hsv, lower, upper)
img = cv2.bitwise_and(img,img, mask= mask)


img = img.reshape((img.shape[0] * img.shape[1],3)) #represent as row*column,channel number
clt = KMeans(n_clusters=5) #cluster number
clt.fit(img)

hist = find_histogram(clt)
bar = plot_colors2(hist, clt.cluster_centers_)

plt.axis("off")
plt.imshow(bar)
plt.show()
