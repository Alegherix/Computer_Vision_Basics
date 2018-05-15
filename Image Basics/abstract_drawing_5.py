import numpy as np
import cv2

canavas = np.zeros((300,300,3),dtype="uint8")



for i in range(0,25):
    #Sätter radien till ett värde mellan 0-199
    radie = np.random.randint(0,high=200)
    #Genererar 3 värden mellan 0-255, som sedan ska sparas i en lista
    color = np.random.randint(0,high=256,size=(3,)).tolist()
    #Genererar 2stycken random nummer mellan 0-299, samt castar det till en tuple,
    #detta för att värdet för (x,y) måste vara i en tuple, medan randint returnerar en numpy.ndarray
    center = tuple(np.random.randint(0,high=300,size=(2,)))


    cv2.circle(canavas,center,radie,color,-1)

cv2.imshow("Abstract Drawing",canavas)
cv2.waitKey(0)