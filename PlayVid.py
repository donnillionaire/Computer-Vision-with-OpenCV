import numpy as np
import cv2


cap= cv2.VideoCapture('vid.mp4')
print (cap)

cv2.destroyAllWindows()
while (cap.isOpened()):
#	ret,frame = cap.read()
	frame=cap.read()
	print (frame)
	break
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#c=cv2.imshow('frame',gray)
	#if cv2.waitKey(25) & 0xFF == ord('q'):
	#	break
		
print(frame)
cap.release()
cv2.destroyAllWindows()

