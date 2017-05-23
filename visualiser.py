import numpy as np
import cv2
import cv2.cv as cv
import random
import marshal

font = cv2.FONT_HERSHEY_SIMPLEX
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cv2.namedWindow('rect')

pp =[320,240]
rect = np.zeros((480,640,3))
liste = []

fp = open("Output.txt")
lines = fp.readlines() 
ll = []
model = []
for line in lines:
    ll.append(int(line))

for i in range(len(ll)):
    if i % 3 == 0:
        model.append((ll[i],ll[i+1],ll[i+2]))
print(model)

modelAleatoire = []
for i in range(50):
    modelAleatoire.append((random.randint(50, 350),random.randint(50, 350),random.randint(10, 500)))

def analog(p):
    return (float(hg[0])+440/(640/float(p[0])),float(hg[1])+330/(480/float(p[1])))

def analogGen(model, p3d):
    maxProf = max(ref[2] for ref in model)
    minProf = min(ref[2] for ref in model)


    x = p3d[0]
    y = p3d[1]
    z = p3d[2]
    rapport = float((maxProf-z))/float((maxProf-minProf))
    proj1 = (x,y)
    proj2 = analog((x,y))
    (xx,yy) = barycentre(proj1,proj2, rapport)
    return (xx,yy)

def drawModel(model, rect):
    for m in model:
        cv2.circle(rect, analogGen(model , m), 2, (0,255,0), 2)

	#for i in range(len(model)-1):
    		#cv2.line(rect ,analogGen(model, model[i]),analogGen(model, model[i+1]),(0,255,255),2)



def barycentre((a,b), (c,d), p):
    return (int(p*a+(1-p)*c), int(p*b+(1-p)*d))




while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray,cv.CV_HOUGH_GRADIENT,1,20)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #cercles
    for xy in liste:
        cv2.circle(rect,xy,2,(0,0,255),3)
    try:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            liste.append((i[0],i[1]))    
            # draw the center of the circle
    except:
        pass
    
    #visages
    for (x,y,w,h) in faces:
        point = [int(0.5*(x+x+w)),int(0.5*(y+y+h))]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img,'Face',(x+h/4,y+w+30), font, 1,(255,0,0),1,cv2.CV_AA)
        cv2.circle(img, (point[0], point[1]), 2, (0,255,0), 2)

        rect = np.zeros((480,640,3))

        m = [int(0.5*(y+y+h)),640-int(0.5*(x+x+w))]
        hd = (m[1]+220,m[0]-165)
        hg = (m[1]-220,m[0]-165)
        bd = (m[1]+220,m[0]+165)
        bg = (m[1]-220,m[0]+165)
        milieu = (int(0.5*(bg[0]+hd[0])),int(0.5*(bg[1]+hd[1])))

        def mid(x,y):
            return (int(0.5*(x[0]+y[0])) , int(0.5*(x[1]+y[1])))

        cv2.circle(rect,(pp[0],pp[1]), 2, (0,0,255), 30)
        #Cube
        ec = (320,240)
        cv2.rectangle(rect, (ec[0]-60, ec[1]-60), (ec[0]+60,ec[1]+60), (255,255,255), 1)
        
        centre = mid(mid(milieu,ec), ec)
        cv2.rectangle(rect, (centre[0]-60,centre[1]-60), (centre[0]+60,centre[1]+60), (255,255,255), 1)
        hd1 = (ec[1]+140,ec[0]-140)
        hg1 = (ec[1]+20,ec[0]-140)
        bd1 = (ec[1]+140,ec[0]-20)
        bg1 = (ec[1]+20,ec[0]-20)

        hd2 = (centre[0]+60,centre[1]-60)
        hg2 = (centre[0]-60,centre[1]-60)
        bd2 = (centre[0]+60,centre[1]+60)
        bg2 = (centre[0]-60,centre[1]+60)
        cv2.line(rect ,bg1,bg2,(255,255,255),1)
        cv2.line(rect ,bd1,bd2,(255,255,255),1)
        cv2.line(rect ,hg1,hg2,(255,255,255),1)
        cv2.line(rect ,hd1,hd2,(255,255,255),1)



        #main rectangle
        cv2.rectangle(rect,(m[1]-220,m[0]-165),(m[1]+220,m[0]+165),(255,255,255),3)

        #line vertical
        for i in range(1,22):
            if i%2==1:
                cv2.line(rect ,(29*i,0),(hg[0]+20*i,hg[1]),(255,255,255),1)
                cv2.line(rect ,(29*i,480),(bg[0]+20*i,bg[1]),(255,255,255),1)
        for i in range(1,24):
            if i%2==1:
                cv2.line(rect ,(0,20*i),(hg[0],hg[1]+14*i),(255,255,255),1)
                cv2.line(rect ,(640,20*i),(hd[0],hd[1]+14*i),(255,255,255),1)
        #line horiz
        #haut
        p1=mid(hg,(0,0))
        p1_=mid(hd,(640,0))
        p2 = mid((0,0),p1)
        p2_=mid((640,0), p1_)
        p3=mid(hg,p1)
        p3_= mid(hd,p1_)
        cv2.line(rect ,p1,p1_,(255,255,255),1)
        cv2.line(rect ,p2,p2_,(255,255,255),1)
        cv2.line(rect ,p3,p3_,(255,255,255),1)
        #bas
        q1=mid(bg,(0,480))
        q1_=mid(bd,(640,480))
        q2 = mid((0,480),q1)
        q2_=mid((640,480), q1_)
        q3=mid(bg,q1)
        q3_= mid(bd,q1_)
        cv2.line(rect ,q1,q1_,(255,255,255),1)
        cv2.line(rect ,q2,q2_,(255,255,255),1)
        cv2.line(rect ,q3,q3_,(255,255,255),1)
        #gauche
        r1=mid((0,0),hg)
        r1_=mid((0,480),bg)
        r2 = mid((0,0),r1)
        r2_=mid((0,480), r1_)
        r3=mid(hg,r1)
        r3_= mid(bg,r1_)
        cv2.line(rect ,r1,r1_,(255,255,255),1)
        cv2.line(rect ,r2,r2_,(255,255,255),1)
        cv2.line(rect ,r3,r3_,(255,255,255),1)
        #droite
        r1=mid((640,0),hd)
        r1_=mid((640,480),bd)
        r2 = mid((640,0),r1)
        r2_=mid((640,480), r1_)
        r3=mid(hd,r1)
        r3_= mid(bd,r1_)
        cv2.line(rect ,r1,r1_,(255,255,255),1)
        cv2.line(rect ,r2,r2_,(255,255,255),1)
        cv2.line(rect ,r3,r3_,(255,255,255),1)


        drawModel(modelAleatoire, rect)


    cv2.imshow('img',img)
    cv2.imshow("rect", rect)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
