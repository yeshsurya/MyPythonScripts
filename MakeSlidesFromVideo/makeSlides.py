# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 10:53:51 2019

@author: 212744433
"""

#author : Yeshwanth

import cv2
import imutils
#------For capturing slow video from webcam-------#
#capture = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#output = cv2.VideoWriter('slowmotion.mp4',fourcc,5,(640,480))

#while True:
#    ret, frame = capture.read()
#    output.write(frame)
#    cv2.imshow('frame',frame)
#    if cv2.waitKey(1) & 0xFF == ord('x'):
#        break

#capture.release()
#output.release()
#cv2.destroyAllWindows()

#------------------------------------------------#
#--------Capturing individual frames 
vidcap = cv2.VideoCapture('slowmotion.mp4')
vs = vidcap
success,firstFrame = vidcap.read()
count = 0
cnts = 0
while success:
  success,frame = vs.read()
  if frame is None:
    break
  frame = imutils.resize(frame, width=500)
  gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  gray = cv2.GaussianBlur(gray, (21, 21), 0)
 
	# if the first frame is None, initialize it
  if firstFrame is None:
    firstFrame = gray
    continue
    # compute the absolute difference between the current frame and
	# first frame
  try:
      frameDelta = cv2.absdiff(firstFrame, gray)
      thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
      thresh = cv2.dilate(thresh, None, iterations=2)
      cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
      cv2.CHAIN_APPROX_SIMPLE)
      cnts = imutils.grab_contours(cnts)
  except:
      pass
  
  if cnts > 0:
        cv2.imwrite("frameDelta%d" % count,frameDelta)
        cv2.imwrite("gray%d"%count,gray)
        cv2.imwrite("thresh%d"%count,thresh)
        count= count + 1
	# loop over the contours
	#for c in cnts:
		# if the contour is too small, ignore it
		#if cv2.contourArea(c) < args["min_area"]:
		#	continue
 
		# compute the bounding box for the contour, draw it on the frame,
		# and update the text
		#(x, y, w, h) = cv2.boundingRect(c)
		#cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		#text = "Occupied"
    # draw the text and timestamp on the frame
	#cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
	#	cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	#cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
	#	(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
 
	# show the frame and record if the user presses a key
	#cv2.imshow("Security Feed", frame)
	#cv2.imshow("Thresh", thresh)
	#cv2.imshow("Frame Delta", frameDelta)
  key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key is pressed, break from the lop
  if key == ord("q"):
    break
#while success:
  #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  #success,image = vidcap.read()
  #print('Read a new frame: ', success)
  #count += 1