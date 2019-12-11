import numpy as np
import cv2


cap= cv2.VideoCapture('2.mp4')

#define the codec and create Video Writer object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
outputObject = cv2.VideoWriter('3t.avi', fourcc, 20.0, (1280,720))



while (cap.isOpened()):
	ret,frame = cap.read()
	#frame=cap.read()
	#print (frame) printing frames in matrix form
	#break
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame',gray)
	if cv2.waitKey(30) & 0xFF == ord('q'):
		break
		
#release everything after the job is done
out.release()

cap.release()
cv2.destroyAllWindows()

