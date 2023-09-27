import cv2

cat_cascade = cv2.CascadeClassifier('data/haarcascade_frontalcatface.xml')

img = cv2.imread('data/cat.jpeg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cats = cat_cascade.detectMultiScale(gray,1.1,3)

print("Cats detected: ",len(cats))

