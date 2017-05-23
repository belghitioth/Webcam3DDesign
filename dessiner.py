import cv2
import numpy as np
import cv2.cv as cv
import sys

cap = cv2.VideoCapture(0)
rect = np.zeros((480,640,3))
l = []
res = ""
def draw(l, im):
	for i in rage(len(l) -1):
		cv2.circle(im,(l[i][0],l[i][1]),2,(0,0,255),2)
		cv2.line(im,(l[i][0],l[i][1]),(l[i+1][0],l[i+1][1]),(0,0,255),2)

while 1:


	ret, img = cap.read()
	img = cv2.medianBlur(img,5)

	cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	circles = cv2.HoughCircles(cimg,cv.CV_HOUGH_GRADIENT,1,100)
	try:
		circles = np.uint16(np.around(circles))
		for i in circles[0,:]:
			cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
			rect = np.zeros((480,640,3))
			l.append(i)
			cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
		for i in range(len(l) -1):
			cv2.circle(rect,(640-l[i][0],l[i][1]),3,(0,0,255),-1)
	except:
		pass
	out = open("Output.txt", "w")

	cv2.imshow('detected circles',cimg)
	cv2.imshow(' circles',rect)


	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

for i in l:
	res +=str(i[0]) + "\n"
	res +=str(i[1]) + "\n"
	res +=str(i[2]) + "\n"

f = open("Output.txt", "w")
f.write(res)
f.close()
print(l)
cv2.destroyAllWindows()
