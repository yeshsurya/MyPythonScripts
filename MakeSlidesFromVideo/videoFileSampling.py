# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:45:53 2019

@author: 212744433
"""

import cv2
def get_match_confidence(img1, img2, mask=None):
    if img1.shape != img2.shape:
        return False
    ## first try, using absdiff
    # diff = cv2.absdiff(img1, img2)
    # h, w, d = diff.shape
    # total = h*w*d
    # num = (diff<20).sum()
    # print 'is_match', total, num
    # return num > total*0.90
    if mask is not None:
        img1 = img1.copy()
        img1[mask!=0] = 0
        img2 = img2.copy()
        img2[mask!=0] = 0
    ## using match
    match = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
    _, confidence, _, _ = cv2.minMaxLoc(match)
    # print confidence
    return confidence 

cap = cv2.VideoCapture('linearcombinations.mp4')
framerate = 30
framecount = 0
success, prevImage = cap.read()
while success:
    # Capture frame-by-frame
    success, presImage = cap.read()
    framecount += 1

    # Check if this is the frame closest to 10 seconds
    if framecount % 25 == 0:
      diff = get_match_confidence(presImage,prevImage)
      if diff < 0.8 :
        cv2.putText(presImage, "MatchConf With Prev Image: {}".format(diff), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.imwrite('image%d.jpg'%framecount,presImage)
        prevImage = presImage
      print(diff)
      

    # Check end of video
    if cv2.waitKey(1) & 0xFF == ord('q'):
          break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()