import numpy as np
import cv2


cap= cv2.VideoCapture('vid.mp4')


cv2.destroyAllWindows()


while (cap.isOpened()):
	ret,frame = cap.read()
	#frame=cap.read()
	#print (frame) printing frames in matrix form
	#break
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame',gray)
	if cv2.waitKey(50) & 0xFF == ord('q'):
		break
		

cap.release()
cv2.destroyAllWindows()

